# Chemical Variational Autoencoder
## Model identifiers
- Slug: chemical-vae
- Ersilia ID: eos3ae7
- Tags: generative

# Model description
Short description of the model in one or two sentences.
- Input: SMILES
- Output: List of SMILES generated for each SMILES input
- Model type: Generative
- Training set: [250,000 random molecules from ZINC database](https://pubs.acs.org/doi/full/10.1021/ci3001277)
- Mode of training: Pretrained

# Source code
Gómez-Bombarelli, R. et al. Automatic Chemical Design Using a Data-Driven Continuous Representation of Molecules. ACS Cent. Sci. 4, 268–276 (2018).

- Code: https://github.com/aspuru-guzik-group/chemical_vae
- Checkpoints: 
    - [Encoder](model/checkpoints/zinc_encoder.h5)
    - [Decoder](model/checkpoints/zinc_decoder.h5)
    - [Property prediction](model/checkpoints/zinc_prop_pred.h5)

# License
The GPL-v3 license applies to all parts of the repository that are not externally maintained libraries. This repository uses the externally maintained library "chemical_vae" and licensed under an Apache-2.0 License.
# History 
- This model was downloaded in 8/30/2022.
- Modifications to the (chemvae)[model/framework/code/chemvae] folder from the original repository were made on 8/31/2022.
- The model was fully incorporated on 9/1/2022.

# About us
The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
