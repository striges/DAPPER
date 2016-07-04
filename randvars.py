from common import *


class GaussRV:
  def __init__(self,mu=0,C=0,m=None):
    # Set mu
    assert is1d(mu)
    self.mu = asarray(mu).squeeze()
    if m is not None:
      if self.mu.size == 1 and m > 1:
        self.mu = self.mu * ones(m)
      else:
        assert self.mu.size == m
    # Set C
    self.is_random = True
    if isinstance(C,CovMat):
      self.C = C
    else:
      if C is 0:
        self.is_random = False
      if np.isscalar(C):
        self.C = CovMat(C * np.ones_like(self.mu),'diag')
      else:
        self.C = CovMat(C)
    # Revise mu
    if self.mu.size == 1 and self.C.m > 1:
      self.mu = self.mu * ones(self.C.m)
    else:
      assert self.mu.size == self.C.m
    # Set length
    self.m = self.mu.size

  def sample(self,N):
    if not self.is_random:
      D = zeros((N,self.m))
    else:
      D = randn((N,self.m)) @ self.C.cholU
    return self.mu + D

  def __str__(self):
    s = []
    printable = ['mu','C']
    for k in printable:
      s.append('{}:\n'.format(k) + str(getattr(self,k)))
    return '\n'.join(s)

  def __repr__(self):
      return self.__str__()

    

class RV:
  def __init__(self,data):
    self.pdf = None
    self.cdf = None
    self.sampling_func = None
    self.sample_file = None
  #...
  def sample(self,N):
    if self.is0:
      E = zeros(self.m, N)
    elif self.sampling_func:
      return self.sampling_func(N)
    elif self.cdf:
      pass
      # multivariate CDF sampling
    elif self.pdf:
      pass
      # A-R sampling



