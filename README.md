# Variational autoencoder for small molecule generation

This variational autoencoder (VAE) for chemistry uses an encoder-decoder-predictor framework to predict new small molecules. The input SMILES molecule is converted into a continuous vector, and the decoder converts this molecular representation back to a discrete SMILES. These continuous molecular representations allow for simple operations to generate new chemical matter. The decoder is constrained to produce valid molecules. In addition, a predictor estimates the chemical properties of the molecules represented as continuous vectors (logP, QED, synthetic accessibility). The chemicalVAE was trained on 250k drugs from ZINC.

This model was incorporated on 2022-08-13.

## Information
### Identifiers
- **Ersilia Identifier:** `eos3ae7`
- **Slug:** `chemical-vae`

### Domain
- **Task:** `Sampling`
- **Subtask:** `Generation`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Compound generation`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `20`
- **Output Consistency:** `Variable`
- **Interpretation:** Compounds generated based on the input molecule

### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos3ae7](https://hub.docker.com/r/ersiliaos/eos3ae7)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos3ae7.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos3ae7.zip)

### Resource Consumption


### References
- **Source Code**: [https://github.com/aspuru-guzik-group/chemical_vae](https://github.com/aspuru-guzik-group/chemical_vae)
- **Publication**: [https://pubs.acs.org/doi/10.1021/acscentsci.7b00572](https://pubs.acs.org/doi/10.1021/acscentsci.7b00572)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2018`
- **Ersilia Contributor:** [brosular](https://github.com/brosular)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [Apache-2.0](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos3ae7
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos3ae7
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
