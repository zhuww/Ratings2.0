import numpy as np

import base
from rating_classes import profile

class PeakOverRMSRater(base.BaseRater):
    short_name = "peakoverrms"
    long_name = "Peak Over RMS Rating"
    description = "Compute the peak amplitude of the profile divided" \
                  "by the RMS amplitude. Specifically, compute " \
                  "(max(profile)-median(profile))/std(profile)."
    version = 3
    
    rat_cls = profile.ProfileClass()

    def _compute_rating(self, cand):
        """Return a rating for the candidate. The rating value is 
            the profile peak divided by its RMS.

            Input:
                cand: A Candidate object to rate.

            Output:
                value: The rating value.
        """
        prof = cand.profile
        return (np.amax(prof)-np.median(prof))/np.std(prof)

Rater = PeakOverRMSRater
