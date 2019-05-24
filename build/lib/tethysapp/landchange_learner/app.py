from tethys_sdk.base import TethysAppBase, url_map_maker


class LandchangeLearner(TethysAppBase):
    """
    Tethys app class for Landchange Learner.
    """

    name = 'Landchange Learner'
    index = 'landchange_learner:home'
    icon = 'landchange_learner/images/landchange_icon.png'
    package = 'landchange_learner'
    root_url = 'landchange-learner'
    color = '#4b870a'
    description = 'Created to work with Landsat data.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='landchange-learner',
                controller='landchange_learner.controllers.home'
            ),
        )

        return url_maps
