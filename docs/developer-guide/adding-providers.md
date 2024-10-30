# Extending service functionality
## Adding new providers
### Introduction

This documentation describes the process of adding a new profanity filtering provider to the system. The implementation is based on creating a class that inherits from FilteringProvider and integrating it into ProviderManager.
Steps to Add a New Provider
#### Define the Provider Class

Create a new class that will inherit from FilteringProvider. Be sure to implement the abstract methods _censor_text and _reload_word_list.

Example:

```python

from dataclasses import dataclass
from your_library import YourBackend  # Import the necessary backend

@dataclass
class YourFilterProvider(FilteringProvider):
    backend = YourBackend()

    async def _censor_text(self, text: str) -> str:
        # Logic for text filtering
        return self.backend.censor(text)

    async def _reload_word_list(self, words: list[str]):
        # Update the list of profanity words
        self.backend.update_word_list(words)
```
#### Add Provider Settings

If necessary, add settings for your new provider. To do this, create a settings class that inherits from ProviderSettings or a similar class if one exists.

Example:
```python
from service.filtering.models import BaseProviderSettings

class YourFilterProviderSettings(BaseProviderSettings):
    # Add the necessary fields
    pass
```
#### Register the Provider in the Manager

Add the new provider to the ProviderManager class. Update the get_provider method to return an instance of your new provider when requested.

Example:
```python

from service.filtering.providers.your_filter import YourFilterProvider

class ProviderManager:
    # ...

    async def get_provider(self, provider_type: ProviderTypes) -> FilteringProvider:
        match provider_type:
            # ...
            case ProviderTypes.YOUR_FILTER_PROVIDER:
                config = await YourFilterProviderSettings.get_solo()
                return YourFilterProvider(
                    # Pass the necessary configuration parameters
                )
```
#### Update the Provider Types Enumeration

Don’t forget to add the new provider type to ProviderTypes so that your system can recognize it.
```python

class ProviderTypes(str, Enum):
    # ...
    YOUR_FILTER_PROVIDER = "YOUR_FILTER_PROVIDER"
```
