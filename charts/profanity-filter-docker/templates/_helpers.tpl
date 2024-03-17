{{/*
Return the proper api image
*/}}
{{- define "api.image" -}}
{{ include "common.images.image" ( dict "imageRoot" .Values.api.image ) }}
{{- end -}}

{{/*
Render full env for api
*/}}
{{- define "env" -}}
- name: POSTGRES_USER
  value: {{ .Values.postgresql.auth.username | quote }}
- name: POSTGRES_PASSWORD
  value: {{ .Values.postgresql.auth.password | quote }}
- name: POSTGRES_HOST
  value: {{ include "common.names.fullname" . }}-postgresql
- name: POSTGRES_PORT
  value: "5432"
- name: POSTGRES_DATABASE
  value: {{ .Values.postgresql.auth.database | quote }}
{{- end -}}

{{/*
Generate a default fully qualified job name.
Due to the job only being allowed to run once, we add the chart revision so helm
upgrades don't cause errors trying to create the already ran job.
Due to the helm delete not cleaning up these jobs, we add a random value to
reduce collision
*/}}
{{- define "migrations.jobname" -}}
{{- $name := include "common.names.fullname" . | trunc 55 | trimSuffix "-" -}}
{{- printf "%s-%s-%d" $name "migrations" .Release.Revision | trunc 63 | trimSuffix "-" -}}
{{- end -}}


{{/*
Render image for wait-postgres init container
*/}}
{{- define "waitPostgresInitContainer.image" -}}
{{ include "common.images.image" (dict "imageRoot" .Values.backend.waitPostgres.image "global" .Values.global )}}
{{- end -}}

{{/*
Render init container for wait-postgres
*/}}
{{- define "waitPostgresInitContainer" -}}
- name: wait-postgres
  image: {{ include "backend.waitPostgresInitContainer.image" . }}
  imagePullPolicy: {{ .Values.backend.waitPostgres.image.pullPolicy | quote }}
  command:
  - sh
  - -ec
  - |
    until (pg_isready); do
      sleep 1
    done
  env:
  - name: PGPASSWORD
    value: {{ .Values.backend.postgres.password|quote }}
  - name: PGHOST
    value: {{ .Values.backend.postgres.host|quote }}
  - name: PGPORT
    value: {{ .Values.backend.postgres.port|quote }}
  - name: PGUSER
    value: {{ .Values.backend.postgres.user|quote }}
  {{- with .Values.backend.waitPostgres.resources }}
  resources: {{- toYaml . | nindent 4 }}
  {{- end }}
{{- end -}}

{{/*
Render init container for migrations waiting
*/}}
{{- define "backend.waitMigrationsInitContainer" -}}
- name: wait-migrations
  image: {{ include "backend.image" . }}
  imagePullPolicy: {{ include "backend.imagePullPolicy" . }}
  command:
  - sh
  - -ec
  - |
    until (python manage.py migrate --check); do
      sleep 1
    done
  env: {{- include "backend.renderEnv" . | nindent 4 }}
  {{- if .Values.backend.waitMigrations.resources }}
  resources: {{- toYaml .Values.backend.waitMigrations.resources | nindent 4 }}
  {{- end }}
{{- end -}}

{{/*
Render all init containers for backend
*/}}
{{- define "initContainers" -}}
{{ include "waitPostgresInitContainer" . }}
{{ include "waitMigrationsInitContainer" . }}
{{- end -}}
