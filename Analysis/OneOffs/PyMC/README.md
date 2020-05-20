
# PyMC Examples

- [Trivariate Regression](https://github.com/pointOfive/Home/tree/master/Analysis#bayes-with-pymc3)
- [Experiemental Design](schwartz_farmersdog.pdf)
- More Coming Soon...

Modern Bayesian analysis leverages
- [Probabilistic Programming](https://docs.pymc.io/)
  - with automatic MCMC posterior sampler construction and no need to manually define
    - Metropolis-Hastings Accept-Reject 
    - Gibbs sampler full conditionals
- [Hamiltonian Monte Carlo](https://arxiv.org/abs/1701.02434) (HMC) Posterior Sampling
  - which greatly increases sampling speed
  - the [No-U-Turn Sampler](https://arxiv.org/abs/1111.4246) (NUTS) is a popular/ubiquetous example of this
- Variational Inference 
  - which even further increases speed
  - by optimizing a KL-Divergence target rather than purusing MCMC integration