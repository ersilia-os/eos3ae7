# Variational autoencoder for small molecule generation

This variational autoencoder (VAE) for chemistry uses an encoder-decoder-predictor framework to predict new small molecules. The input SMILES molecule is converted into a continuous vector, and the decoder converts this molecular representation back to a discrete SMILES. These continuous molecular representations allow for simple operations to generate new chemical matter. The decoder is constrained to produce valid molecules. In addition, a predictor estimates the chemical properties of the molecules represented as continuous vectors (logP, QED, synthetic accessibility). The chemicalVAE was trained on 250k drugs from ZINC.

## Identifiers

* EOS model ID: `eos3ae7`
* Slug: `chemical-vae`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Generative`
* Output: `Compound`
* Output Type: `String`
* Output Shape: `Flexible List`
* Interpretation: Compounds generated based on the input molecule

## References

* [Publication](https://pubs.acs.org/doi/10.1021/acscentsci.7b00572)
* [Source Code](https://github.com/aspuru-guzik-group/chemical_vae)
* Ersilia contributor: [brosular](https://github.com/brosular)

## Citation

If you use this model, please cite the [original authors](https://pubs.acs.org/doi/10.1021/acscentsci.7b00572) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a Apache-2.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!