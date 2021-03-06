registered_raters = ["duty_cycle", \
                     "pulse_width", \
                     "wiggle", \
                     "known_pulsar", \
                     "mains_rfi", \
                     "peak_over_rms", \
                     "prepfold_sigma", \
                     "dm_comparison_std", \
                     "dm_comparison_chisqr", \
                     "dm_comparison_peak", \
                     "gaussian_amplitude", \
                     "gaussian_goodness", \
                     "gaussian_fwhm", \
                     "frac_good_subbands", \
                     "frac_good_intervals", \
                     "subbands_snrstd", \
                     "subints_snrstd", \
                     "multigauss_number", \
                     "multigauss_goodness", \
                     "ubc_pfd_ai"]

__all__ = registered_raters

for rater_name in registered_raters:
    __import__(rater_name, globals())
