# Downloading NMDC Data via Globus

[Globus](https://globus.org) provides a mechanism to download NMDC data using high-bandwidth managed transfers. Globus has an automated point-and-click interface that lets you schedule a bulk transfer to your own machine or another compute center. You can learn more about using Globus to transfer data, by reading the [Globus documentation](https://www.globus.org/data-transfer).

## Globus Collections

NMDC collections are publicly visible to everyone that has a [Globus ID](https://www.globusid.org/create).

### NERSC

To access NMDC data housed at NERSC, you can use the ["NMDC" collection](https://app.globus.org/file-manager?origin_id=72dd396a-2242-11ec-a0a4-6b21ca6daf73&origin_path=%2F).

In that collection, NMDC data are organized by _NMDC identifiers_. This collection serves up the same contents as `https://data.microbiomedata.org/data/` does, so any file path underneath that base URL can be mapped to the equivalent file in Globus.

### EMSL

To access NMDC data housed at EMSL, you can use the ["NMDC Bulk Data Cache" collection](https://app.globus.org/file-manager?origin_id=07de22e4-6c17-4bd2-86bc-49fe5ddb2070&origin_path=%2F).

In that collection, NMDC data are organized by _omics types_. This collection serves up the same contents as `https://nmdcdemo.emsl.pnnl.gov/` does, so any file path underneath that base URL can be mapped to the equivalent file in Globus.
