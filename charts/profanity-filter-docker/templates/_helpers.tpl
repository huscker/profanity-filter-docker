{{/*
Return the proper api image
*/}}
{{- define "api.image" -}}
{{ include "common.images.image" ( dict "imageRoot" .Values.api.image ) }}
{{- end -}}

{{/*
Render full env for api
*/}}
{{- define "api.renderEnv" -}}
- name: POSTGRES_USER
  value: {{ .Values.postgresql.auth.username | quote }}
- name: POSTGRES_PASSWORD
  value: {{ .Values.postgresql.auth.password | quote }}
- name: POSTGRES_HOST
  value: {{ include "common.names.fullname" . }}-postgresql
- name: POSTGRES_PORT
  value: 5432
- name: POSTGRES_DATABASE
  value: {{ .Values.postgresql.auth.database | quote }}
- name: REDIS_USER
  value: {{ .Values.redis.auth. | quote }}
- name: REDIS_PASSWORD
  value: {{ .Values.redis.auth.password | quote }}
- name: REDIS_HOST
  value: {{ include "common.names.fullname" . }}-redis
- name: REDIS_PORT
  value: 6379
{{- end -}}
