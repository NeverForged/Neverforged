


class WebTemp(object):
    '''
    Not even going to TRY to make this pep8 compliant; too much css and
    '''

    def __init__(self):
        self.end = '<br><br</body></html>'
        self.start = '''
            <!DOCTYPE html>
            <!-- saved from url=(0038)https://darinlasota.wixsite.com/mysite -->
            <html class=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=Edge">



            <title>mysite</title>
            <meta name="fb_admins_meta_tag" content="">
            <link rel="shortcut icon" href="https://www.wix.com/favicon.ico" type="image/x-icon">
            <link rel="apple-touch-icon" href="https://www.wix.com/favicon.ico" type="image/x-icon">
                <script type="text/javascript">
                var santaBase = 'https://static.parastorage.com/services/santa/1.2367.27';
                            var clientSideRender = true;
                            </script>

            <script defer="" src="./mysite_files/require.min.js.download"></script>
            <script defer="" src="./mysite_files/main-r.min.js.download"></script>


            <link rel="prefetch" href="./mysite_files/react-with-addons.min.js.download">
            <link rel="prefetch" href="./mysite_files/TweenMax.min.js.download">
            <link rel="prefetch" href="./mysite_files/lodash.min.js.download">

            <link rel="preconnect" href="https://static.wixstatic.com/">
            <link rel="preconnect" href="https://fonts.googleapis.com/">
                <meta http-equiv="X-Wix-Renderer-Server" content="app-jvm54a.42.wixprod.net">
            <meta http-equiv="X-Wix-Meta-Site-Id" content="7b72538d-d23e-4b49-8395-5abc134596d8">
            <meta http-equiv="X-Wix-Application-Instance-Id" content="383d214d-2df4-43f9-b753-fd6ff64dec18">
            <meta http-equiv="X-Wix-Published-Version" content="57">

            <meta http-equiv="etag" content="595829b736b6d7dc23388e12267b36bc">

            <meta property="og:type" content="article">

            <meta property="og:site_name" content="mysite">
            <meta name="SKYPE_TOOLBAR" content="SKYPE_TOOLBAR_PARSER_COMPATIBLE">

            <meta id="wixMobileViewport" name="viewport" content="width=980, user-scalable=yes">





                <script>
                // BEAT MESSAGE
                try {
                    window.wixBiSession = {
                        initialTimestamp : Date.now(),
                                    viewerSessionId: 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c)
                                { var r = Math.random()*16|0, v = c == 'x' ? r : (r&0x3|0x8); return v.toString(16); }
                        )
                                };
                    (new Image()).src = 'https://frog.wix.com/bt?src=29&evid=3&pn=1&et=1&v=1.2367.27&msid=7b72538d-d23e-4b49-8395-5abc134596d8&vsi=' + wixBiSession.viewerSessionId +
                            '&url=' + encodeURIComponent(location.href.replace(/^http(s)?:\/\/(www\.)?/, '')) +
                            '&isp=0&st=2&ts=0&c=' + wixBiSession.initialTimestamp;
                } catch (e){}
                // BEAT MESSAGE END
            </script>



                <!-- META DATA -->
            <script type="text/javascript">

                var serviceTopology = {"serverName":"app-jvm54a.42.wixprod.net","cacheKillerVersion":"1","staticServerUrl":"https://static.parastorage.com/","usersScriptsRoot":"https://static.parastorage.com/services/wix-users/2.660.0","biServerUrl":"https://frog.wix.com/","userServerUrl":"https://users.wix.com/","billingServerUrl":"https://premium.wix.com/","mediaRootUrl":"https://static.wixstatic.com/","logServerUrl":"https://frog.wix.com/plebs","monitoringServerUrl":"https://TODO/","usersClientApiUrl":"https://users.wix.com/wix-users","publicStaticBaseUri":"https://static.parastorage.com/services/wix-public/1.231.0","basePublicUrl":"https://www.wix.com/","postLoginUrl":"https://www.wix.com/my-account","postSignUpUrl":"https://www.wix.com/new/account","baseDomain":"wix.com","staticMediaUrl":"https://static.wixstatic.com/media","staticAudioUrl":"https://music.wixstatic.com/mp3","staticDocsUrl":"https://docs.wixstatic.com/ugd","emailServer":"https://assets.wix.com/common-services/notification/invoke","blobUrl":"https://static.parastorage.com/wix_blob","htmlEditorUrl":"http://editor.wix.com/html","siteMembersUrl":"https://users.wix.com/wix-sm","scriptsLocationMap":{"santa-versions":"https://static.parastorage.com/services/santa-versions/1.419.0","dbsm-viewer-app":"https://static.parastorage.com/services/dbsm-viewer-app/1.104.0","wix-music-embed":"https://static.parastorage.com/services/wix-music-embed/1.26.0","santa-resources":"https://static.parastorage.com/services/santa-resources/1.2.0","wixapps":"https://static.parastorage.com/services/wixapps/2.486.0","ecommerce":"https://static.parastorage.com/services/ecommerce/1.203.0","dbsm-editor-app":"https://static.parastorage.com/services/dbsm-editor-app/1.278.0","langs":"https://static.parastorage.com/services/langs/2.568.0","automation":"https://static.parastorage.com/services/automation/1.23.0","web":"https://static.parastorage.com/services/web/2.1229.72","sitemembers":"https://static.parastorage.com/services/sm-js-sdk/1.31.0","js-wixcode-sdk":"https://static.parastorage.com/services/js-wixcode-sdk/1.147.0","tpa":"https://static.parastorage.com/services/tpa/2.1062.0","santa":"https://static.parastorage.com/services/santa/1.2367.27","skins":"https://static.parastorage.com/services/skins/2.1229.72","core":"https://static.parastorage.com/services/core/2.1229.72","santa-members-viewer-app":"https://static.parastorage.com/services/santa-members-viewer-app/1.7.0","ck-editor":"https://static.parastorage.com/services/ck-editor/1.87.3","bootstrap":"https://static.parastorage.com/services/bootstrap/2.1229.72","santa-members-editor-app":"https://static.parastorage.com/services/santa-members-editor-app/1.8.0"},"developerMode":false,"productionMode":true,"staticServerFallbackUrl":"https://sslstatic.wix.com/","staticVideoUrl":"https://video.wixstatic.com/","cloudStorageUrl":"https://static.wixstatic.com/","usersDomainUrl":"https://users.wix.com/wix-users","scriptsDomainUrl":"https://static.parastorage.com/","userFilesUrl":"https://static.parastorage.com/","staticHTMLComponentUrl":"https://darinlasota-wixsite-com.usrfiles.com/","secured":true,"ecommerceCheckoutUrl":"https://www.safer-checkout.com/","premiumServerUrl":"https://premium.wix.com/","digitalGoodsServerUrl":"https://dgs.wixapps.net/","wixCloudBaseDomain":"wix-code.com","mailServiceSuffix":"/_api/common-services/notification/invoke","staticVideoHeadRequestUrl":"https://storage.googleapis.com/video.wixstatic.com","protectedPageResolverUrl":"https://site-pages.wix.com/_api/wix-public-html-info-webapp/resolve_protected_page_urls","mediaUploadServerUrl":"https://files.wix.com/","publicStaticsUrl":"https://static.parastorage.com/services/wix-public/1.231.0"};
                var santaModels = true;
                var rendererModel = {"metaSiteId":"7b72538d-d23e-4b49-8395-5abc134596d8","siteInfo":{"documentType":"UGC","applicationType":"HtmlWeb","siteId":"383d214d-2df4-43f9-b753-fd6ff64dec18","siteTitleSEO":"mysite"},"clientSpecMap":{"2":{"type":"appbuilder","applicationId":2,"appDefinitionId":"3d590cbc-4907-4cc4-b0b1-ddf2c5edf297","instanceId":"49ed1c61-cb33-40b7-a0c0-d2a08005f92e","state":"Initialized"},"13":{"type":"sitemembers","applicationId":13,"collectionType":"Open","collectionFormFace":"Register","smtoken":"a350700ae5332d3774d350e56a1e4a08e06f15718191da86ced21ab71d75428d23ca1ba8aff7ba2444a12d3368a56ccf43b5a839f8ac7516295eba5b85ec1945ee2a215381a7c5973a7d918ec5042f6a135b56826af7a2afa7b720c987a55517afa2616beae3b557ba7d8a95e494da76","smcollectionId":"66ebd3f0-5a97-4dcc-a9e7-514b864ad29a"},"1831":{"type":"public","applicationId":1831,"appDefinitionId":"13c1402c-27f2-d4ab-7463-ee7c89e07578","appDefinitionName":"Wix Restaurants Menus","instance":"8nJgyryLwplsBFLNNGqU_bin5s9SdMBOhXtqqbMhZko.eyJpbnN0YW5jZUlkIjoiYzZmNjUxZGQtYjI1OS00M2QzLWE0M2EtYjQyMDE1MDAzYzQ3IiwiYXBwRGVmSWQiOiIxM2MxNDAyYy0yN2YyLWQ0YWItNzQ2My1lZTdjODllMDc1NzgiLCJzaWduRGF0ZSI6IjIwMTctMDgtMDNUMTU6Mzk6MzQuNzM0WiIsInVpZCI6Ijc1OTY0NTEzLTQ3MjktNDczNC04ZmIzLTI0ODgwMzA0NGYyMyIsInBlcm1pc3Npb25zIjoiT1dORVIiLCJpcEFuZFBvcnQiOiI2NC4xMjUuMTkyLjEzMC80NjgwMSIsInZlbmRvclByb2R1Y3RJZCI6bnVsbCwiZGVtb01vZGUiOmZhbHNlLCJvcmlnaW5JbnN0YW5jZUlkIjoiZWQzMDZjODctNTNmZS00MWFlLWI1YTgtNmUzYmU4ZGE0MTc2IiwiYWlkIjoiNzU5NjQ1MTMtNDcyOS00NzM0LThmYjMtMjQ4ODAzMDQ0ZjIzIiwiYmlUb2tlbiI6ImJkODQwMjUwLTYwNjctMDg5YS0yN2FmLWVlOWMwNjQ1YWE5ZiIsInNpdGVPd25lcklkIjoiNzU5NjQ1MTMtNDcyOS00NzM0LThmYjMtMjQ4ODAzMDQ0ZjIzIn0","sectionUrl":"https:\/\/apps.wixrestaurants.com\/?type=wixmenus.client","sectionMobileUrl":"https:\/\/apps.wixrestaurants.com\/?type=wixmenus.client","sectionPublished":true,"sectionMobilePublished":true,"sectionSeoEnabled":true,"sectionDefaultPage":"","sectionRefreshOnWidthChange":true,"widgets":{"13c1404b-b03b-ee00-84c1-51ae431a537f":{"widgetUrl":"https:\/\/apps.wixrestaurants.com\/?type=wixmenus.client","widgetId":"13c1404b-b03b-ee00-84c1-51ae431a537f","refreshOnWidthChange":true,"mobileUrl":"https:\/\/apps.wixrestaurants.com\/?type=wixmenus.client","appPage":{"id":"menu","name":"Menus","defaultPage":"","hidden":false,"multiInstanceEnabled":true,"order":1,"indexable":true,"fullPage":false,"landingPageInMobile":false,"hideFromMenu":false},"published":true,"mobilePublished":true,"seoEnabled":true,"preFetch":false,"shouldBeStretchedByDefault":false,"shouldBeStretchedByDefaultMobile":false}},"appRequirements":{"requireSiteMembers":false},"isWixTPA":true,"installedAtDashboard":false,"permissions":{"revoked":true}}},"premiumFeatures":[],"geo":"USA","languageCode":"en","previewMode":false,"userId":"75964513-4729-4734-8fb3-248803044f23","siteMetaData":{"preloader":{"uri":"","enabled":false},"adaptiveMobileOn":true,"quickActions":{"socialLinks":[],"colorScheme":"dark","configuration":{"quickActionsMenuEnabled":false,"navigationMenuEnabled":true,"phoneEnabled":false,"emailEnabled":false,"addressEnabled":false,"socialLinksEnabled":false}},"contactInfo":{"companyName":"","phone":"","fax":"","email":"","address":""}},"runningExperiments":{"appMarketCache":"new","sv_textLinkWhiteList":"new","sv_platform1":"new","reactAppMarketModals":"new","sv_hoverBox":"new","sv_dpages":"new","clickToAction_email":"new","sv_smSocialLoginEnabledByDefault":"new","sv_ampLinkTag":"new","connectionsData":"new","sv_twitterMetaTags":"new","sv_mobileBgFixed":"new","sv_blogTranslateErrorMessage":"new","sv_listsBatchRequest":"new","sv_blogRelatedPosts":"new","sv_expandModeBi":"new","unescapeHeadTags":"old","sv_reportPerformance":"new","clickToAction_url":"new","sv_cssDesignData":"new","useBeaconForPerformanceEvent":"new","sv_blogCountersHttpsRequest":"new","viewPortImageLoadingBi":"3000","sv_webpJPGSupport":"new","sv_addFirstTimeRenderBiEvents":"new","reactAppMarket":"new","sv_delelteItemsRecursively":"new","fontsTrackingInViewer":"new","tpaHideFromMenu":"new","sv_blogSocialCounters":"new","sv_addJsonldToHeadForSEO":"new","clickToAction_phone":"new","viewPortImageLoading":"new","allowScriptTagTypeJsonOnSeoMetatag":"old","sv_fixColorOfHatulOnHover":"new","autosaveTpaSettle":"new","retryOnConcurrencyError":"new","permalinkWithoutDate":"new","sv_faviconFromServer":"new","sv_mobileBG":"new","pageListNewFormat":"new","sv_blogAuthorAsALink":"new","se_ignoreBottomBottomAnchors":"new","packagescache":"new","fontScaling":"new","autosaveWixappsSettle":"new","sv_tpaMultiWidget":"new","hashPasswordOnServer":"new","sv_tpaAddChatApp":"new","sv_blogOldUrlShareFix":"new","sv_SendSdkMethodBI":"new","sv_addBorderToElementBounds":"new","sv_partialReLayout":"new","sv_blogNotifySocialCounters":"new","sv_qab":"new","sv_blogLikeCounters":"new","sv_robotsIndexingMetaTag":"new","sv_ignoreBottomBottomAnchors":"new","sv_grid":"new","sv_NewFacebookConversionPixel":"new","sv_mobileSpachtelPattern":"new","sv_tpaPerformanceBi":"new","sv_unpackTextMeasureByMinHeight":"new","sv_alwaysEnableMobileZoom":"new"},"urlFormatModel":{"format":"slash","forbiddenPageUriSEOs":["app","apps","_api","robots.txt","sitemap.xml","feed.xml","sites"],"pageIdToResolvedUriSEO":{}},"passwordProtectedPages":[],"useSandboxInHTMLComp":true,"siteMediaToken":"eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcHA6MzQ2NjQ5MDcwMDI5NzIwNiIsInN1YiI6InVzZXI6NzU5NjQ1MTMtNDcyOS00NzM0LThmYjMtMjQ4ODAzMDQ0ZjIzIiwiYXVkIjoidXJuOnNlcnZpY2U6ZmlsZS51cGxvYWQiLCJleHAiOjE1MDIzNzk1NzQsImlhdCI6MTUwMTc3NDc3NCwianRpIjoiOU13VmRkVXNvNURNVWdjN1Q3MVVUdyJ9.xldvFN2VK83-w-UR-fWjClksCijtDXeFg6591MUx5aU","pagesPlatformApplications":{}};
                var publicModel = {"domain":"wixsite.com","externalBaseUrl":"https:\/\/darinlasota.wixsite.com\/mysite","unicodeExternalBaseUrl":"https:\/\/darinlasota.wixsite.com\/mysite","pageList":{"pages":[{"pageId":"izubo","title":"Combat","pageUriSEO":"combat","pageJsonFileName":"759645_fc0cbf3264587adf6643803ba912b17c_53.json"},{"pageId":"v8mea","title":"Home","pageUriSEO":"home","pageJsonFileName":"759645_73e2ed56606020734129589cca4d6703_50.json"},{"pageId":"k6rnh","title":"Items","pageUriSEO":"equipment-inventory","pageJsonFileName":"759645_6ff636a02ddf8e790987ac6ba6461057_57.json"},{"pageId":"alyzs","title":"Notes","pageUriSEO":"notes","pageJsonFileName":"759645_9b8ebd844763fb161e7c6cd7eeab7b79_54.json"},{"pageId":"ja4uq","title":"Persona","pageUriSEO":"appearance-background","pageJsonFileName":"759645_027ec2c9b99442b958a89cc554d42ce5_54.json"},{"pageId":"gyrb2","title":"Abilities","pageUriSEO":"traits","pageJsonFileName":"759645_4805597e3d5d173822cd64706dac4c5e_54.json"}],"mainPageId":"v8mea","masterPageJsonFileName":"759645_c1497210233659223c5a778828112677_57.json","topology":[{"baseUrl":"https:\/\/static.wixstatic.com\/","parts":"sites\/{filename}.z?v=3"},{"baseUrl":"https:\/\/staticorigin.wixstatic.com\/","parts":"sites\/{filename}.z?v=3"},{"baseUrl":"https:\/\/fallback.wix.com\/","parts":"wix-html-editor-pages-webapp\/page\/{filename}"}]},"timeSincePublish":20029,"favicon":"","deviceInfo":{"deviceType":"Desktop","browserType":"Chrome","browserVersion":59},"siteRevision":57,"sessionInfo":{"hs":373347798,"svSession":"2b46761860a62a04efdaac9125a7cbcfde07efc2e2a012b679b04080914bd486295cc0210407cc7999263d270e37b4791e60994d53964e647acf431e4f798bcd1fea8fa11885e36decfdb371e5cd55bbf9016f87826a696fde35aacc94fc2b1c","ctToken":"RDlDYXk0d3JKR2J2Uk1QdHcwUlhHSTN1MWtEY2RIZFdHc1VoQkRISDFrSXx7InVzZXJBZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS81OS4wLjMwNzEuMTE1IFNhZmFyaS81MzcuMzYiLCJ2YWxpZFRocm91Z2giOjE1MDIzNzk1NzQ3MzN9","isAnonymous":false},"metaSiteFlags":[],"siteMembersProtectedPages":[],"indexable":true,"hasBlogAmp":false,"renderTime":1501774774734};



                var googleAnalytics = "UA-2117194-61"
                ;

                var googleRemarketing = "";
                var facebookRemarketing = "";
                var yandexMetrika = "";

            </script>



                        <meta name="fragment" content="!">

                <!-- DATA -->
            <script type="text/javascript">
                var adData = {"topLabel":"<span class=\"smallMusa\">(Wix-Logo) </span>Create a <span class=\"smallLogo\">Wix</span> site!","topContent":"100s of templates<br />No coding needed<br /><span class=\"emphasis spacer\">Start now >></span>","footerLabel":"<div class=\"adFootBox\"><div class=\"siteBanner\" ><div class=\"siteBanner\"><div class=\"wrapper\"><div class=\"bigMusa\">(Wix Logo)</div><div class=\"txt shd\" style=\"color:#fff\">This site was created using </div> <div class=\"txt shd\"><a  href=\"http://www.wix.com?utm_campaign=vir_wixad_live&experiment_id=abtestbanner122400001\" style=\"color:#fff\"> WIX.com. </a></div> <div class=\"txt shd\" style=\"color:#fff\"> Create your own for FREE <span class=\"emphasis\"> >></span></div></div></div></div></div>","adUrl":"http://www.wix.com/lpviral/enviral?utm_campaign=vir_wixad_live&experiment_id=abtestbanner122400001"};
                var mobileAdData = {"footerLabel":"7c3dbd_67131d7bd570478689be752141d4e28a.jpg","adUrl":"http://www.wix.com?utm_campaign=vir_wixad_live&experiment_id=abtestbanner122400001"};
                var usersDomain = "https://users.wix.com/wix-users";
                    </script>
                    <script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="wixCodeInit" src="./mysite_files/wixCodeInit.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="lodash" src="./mysite_files/lodash.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="coreUtils" src="./mysite_files/coreUtils.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="skins" src="./mysite_files/skins.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="components" src="./mysite_files/components.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="core" src="./mysite_files/core.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="mobx" src="./mysite_files/mobx.umd.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="mobx-react" src="./mysite_files/mobx-react.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="TimelineMax" src="./mysite_files/TweenMax.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="animations" src="./mysite_files/animations.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="react" src="./mysite_files/react-with-addons.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="layout" src="./mysite_files/layout.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="wixappsCore" src="./mysite_files/wixappsCore.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="wixappsBuilder" src="./mysite_files/wixappsBuilder.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="tpa" src="./mysite_files/tpa.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="dataFixer" src="./mysite_files/dataFixer.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="siteUtils" src="./mysite_files/siteUtils.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="translationsUtils" src="./mysite_files/translationsUtils.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="hammer" src="./mysite_files/hammer.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="utils" src="./mysite_files/utils.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="fonts" src="./mysite_files/fonts.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="platformUtils" src="./mysite_files/platformUtils-bundle.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="loggingUtils" src="./mysite_files/loggingUtils.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="imageClientLib" src="./mysite_files/imageClientApi.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="swfobject" src="./mysite_files/swfobject.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="santaProps" src="./mysite_files/santaProps.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="displayer" src="./mysite_files/displayer.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="wixUrlParser" src="./mysite_files/wixUrlParser.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="mousetrap" src="./mysite_files/mousetrap.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="DrawSVGPlugin" src="./mysite_files/DrawSVGPlugin.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="reactDOM" src="./mysite_files/react-dom.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="ScrollToPlugin" src="./mysite_files/ScrollToPlugin.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="widgets" src="./mysite_files/widgets.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="render" src="./mysite_files/render.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="reactDOMServer" src="./mysite_files/react-dom-server.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="imageCommon" src="./mysite_files/imageCommon.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="formCommon" src="./mysite_files/formCommon.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="textCommon" src="./mysite_files/textCommon.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="containerCommon" src="./mysite_files/containerCommon.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="socialCommon" src="./mysite_files/socialCommon.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="galleriesCommon" src="./mysite_files/galleriesCommon.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="buttonCommon" src="./mysite_files/buttonCommon.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="compDesignUtils" src="./mysite_files/compDesignUtils.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="mediaCommon" src="./mysite_files/mediaCommon.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="audioCommon" src="./mysite_files/audioCommon.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="skinExports" src="./mysite_files/skinExports.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="compUtils" src="./mysite_files/compUtils.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="fileUploader" src="./mysite_files/fileUploader.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="wixSkinOnly" src="./mysite_files/wixSkinOnly.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="pinItPinWidget" src="./mysite_files/pinItPinWidget.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="siteButton" src="./mysite_files/siteButton.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="popupCloseTextButton" src="./mysite_files/popupCloseTextButton.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="image" src="./mysite_files/image.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="zoomedImage" src="./mysite_files/zoomedImage.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="wPhoto" src="./mysite_files/wPhoto.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="clipArt" src="./mysite_files/clipArt.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="matrixGallery" src="./mysite_files/matrixGallery.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="wRichText" src="./mysite_files/wRichText.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="paginatedGridGallery" src="./mysite_files/paginatedGridGallery.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="container" src="./mysite_files/container.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="radioButton" src="./mysite_files/radioButton.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="radioGroup" src="./mysite_files/radioGroup.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="headerContainer" src="./mysite_files/headerContainer.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="footerContainer" src="./mysite_files/footerContainer.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="screenWidthContainer" src="./mysite_files/screenWidthContainer.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="documentMedia" src="./mysite_files/documentMedia.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="adminLoginButton" src="./mysite_files/adminLoginButton.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="backgroundCommon" src="./mysite_files/backgroundCommon.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="balata" src="./mysite_files/balata.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="datePicker" src="./mysite_files/datePicker.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="contactForm" src="./mysite_files/contactForm.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="subscribeForm" src="./mysite_files/subscribeForm.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="textArea" src="./mysite_files/textArea.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="video" src="./mysite_files/video.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="loginButton" src="./mysite_files/loginButton.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="googleMap" src="./mysite_files/googleMap.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="mediaContainerFactory" src="./mysite_files/mediaContainerFactory.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="soundCloudWidget" src="./mysite_files/soundCloudWidget.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="paypalButton" src="./mysite_files/paypalButton.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="imageButton" src="./mysite_files/imageButton.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="linkBar" src="./mysite_files/linkBar.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="comboBoxInput" src="./mysite_files/comboBoxInput.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="spotifyPlayer" src="./mysite_files/spotifyPlayer.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="spotifyFollow" src="./mysite_files/spotifyFollow.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="twitterFeed" src="./mysite_files/twitterFeed.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="backToTopButton" src="./mysite_files/backToTopButton.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="svgShape" src="./mysite_files/svgShape.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="facebookLike" src="./mysite_files/facebookLike.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="facebookComments" src="./mysite_files/facebookComments.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="facebookLikeBox" src="./mysite_files/facebookLikeBox.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="rssButton" src="./mysite_files/rssButton.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="textInput" src="./mysite_files/textInput.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="tinyMenu" src="./mysite_files/tinyMenu.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="groupContainer" src="./mysite_files/groupContainer.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="pinterestPinIt" src="./mysite_files/pinterestPinIt.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="pinterestFollow" src="./mysite_files/pinterestFollow.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="wTwitterFollow" src="./mysite_files/wTwitterFollow.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="audioPlayer" src="./mysite_files/audioPlayer.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="column" src="./mysite_files/column.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="htmlComponent" src="./mysite_files/htmlComponent.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="deadComponent" src="./mysite_files/deadComponent.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="pmrpc" src="./mysite_files/pm-rpc.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="tweenEngine" src="./mysite_files/tweenEngine.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="multilingual" src="./mysite_files/multilingual.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="color" src="./mysite_files/color.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="zepto" src="./mysite_files/zepto.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="xss" src="./mysite_files/xss.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="bluebird" src="./mysite_files/bluebird.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="coreUtilsLib" src="./mysite_files/coreUtils.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="imageClientApi" src="./mysite_files/imageClientApi.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="facebookShare" src="./mysite_files/facebookShare.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="vKShareButton" src="./mysite_files/vKShareButton.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="youTubeSubscribeButton" src="./mysite_files/youTubeSubscribeButton.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="itunesButton" src="./mysite_files/itunesButton.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="skypeCallButton" src="./mysite_files/skypeCallButton.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="loginSocialBar" src="./mysite_files/loginSocialBar.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="svgCommon" src="./mysite_files/svgCommon.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="flickrBadgeWidget" src="./mysite_files/flickrBadgeWidget.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="wGooglePlusOne" src="./mysite_files/wGooglePlusOne.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="wTwitterTweet" src="./mysite_files/wTwitterTweet.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="mediaPlayer" src="./mysite_files/mediaPlayer.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="mediaControls" src="./mysite_files/mediaControls.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="sliderGallery" src="./mysite_files/sliderGallery.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="slideShowGallery" src="./mysite_files/slideShowGallery.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="singleAudioPlayer" src="./mysite_files/singleAudioPlayer.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="quickActionBar" src="./mysite_files/quickActionBar.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="boxSlideShowSlide" src="./mysite_files/boxSlideShowSlide.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="stripSlideShowSlide" src="./mysite_files/stripSlideShowSlide.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="page" src="./mysite_files/page.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="bgImageStrip" src="./mysite_files/bgImageStrip.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="popupContainer" src="./mysite_files/popupContainer.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="stripContainer" src="./mysite_files/stripContainer.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="stripColumnsContainer" src="./mysite_files/stripColumnsContainer.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="siteBackground" src="./mysite_files/siteBackground.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="hoverBox" src="./mysite_files/hoverBox.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="exitMobileModeButton" src="./mysite_files/exitMobileModeButton.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="tpaGalleries" src="./mysite_files/tpaGalleries.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="internalMarkings" src="./mysite_files/internalMarkings.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="messageView" src="./mysite_files/messageView.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="flashComponent" src="./mysite_files/flashComponent.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="stripSlideShow" src="./mysite_files/stripSlideShow.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="mediaZoom" src="./mysite_files/mediaZoom.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="mobileActionsMenu" src="./mysite_files/mobileActionsMenu.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="imageZoom" src="./mysite_files/imageZoom.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="imageZoomDisplayer" src="./mysite_files/imageZoomDisplayer.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="verticalMenu" src="./mysite_files/verticalMenu.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="dropDownMenu" src="./mysite_files/dropDownMenu.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="menuButton" src="./mysite_files/menuButton.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="infoTip" src="./mysite_files/infoTip.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="pageGroup" src="./mysite_files/pageGroup.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="verticalAnchorsMenu" src="./mysite_files/verticalAnchorsMenu.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="disqusComments" src="./mysite_files/disqusComments.min.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="checkbox" src="./mysite_files/checkbox.min.js.download"></script><style type="text/css">html, body, div, span, applet, object, iframe,
            h1, h2, h3, h4, h5, h6, p, blockquote, pre,
            a, abbr, acronym, address, big, cite, code,
            del, dfn, em, font, img, ins, kbd, q, s, samp,
            small, strike, strong, sub, sup, tt, var,
            b, u, i, center,
            dl, dt, dd, ol, ul, li,
            fieldset, form, label, legend,
            table, caption, tbody, tfoot, thead, tr, th, td,
            nav, button, section, header, footer, title {
              margin: 0;
              padding: 0;
              border: 0;
              outline: 0;
              vertical-align: baseline;
              background: transparent; }

            body {
              font-size: 12px;
              font-family: Georgia, Times, "Times New Roman", serif; }

            textarea, input, select {
              font-size: 12px;
              font-family: "Brush Script MT", cursive;
              box-sizing: border-box; }

            ol, ul {
              list-style: none; }

            blockquote, q {
              quotes: none; }

            ins {
              text-decoration: none; }

            del {
              text-decoration: line-through; }

            table {
              border-collapse: collapse;
              border-spacing: 0; }

            a {
              cursor: pointer;
              text-decoration: none; }

            html, body {
              height: 100%; }

            body {
              overflow-x: auto;
              overflow-y: scroll; }

            .testStyles {
              overflow-y: hidden; }

            .reset-button {
              background: none;
              border: 0;
              outline: 0;
              color: inherit;
              /* cursor: default; */
              font: inherit;
              line-height: normal;
              overflow: visible;
              padding: 0;
              -webkit-appearance: none;
              -webkit-user-select: none;
              -moz-user-select: none;
              -ms-user-select: none; }

            :focus {
              outline: none; }

            .wixSiteProperties {
              -webkit-font-smoothing: antialiased;
              -moz-osx-font-smoothing: grayscale;
              overflow: hidden; }

            .SITE_ROOT {
              min-height: 100%;
              position: relative;
              margin: 0 auto; }

            .POPUPS_ROOT {
              left: 0;
              top: 0;
              width: 100%;
              height: 100%;
              overflow-x: auto;
              overflow-y: scroll;
              position: fixed;
              z-index: 99999; }
              .POPUPS_ROOT.mobile {
                z-index: 1005;
                -webkit-overflow-scrolling: touch; }

            .POPUPS_WRAPPER {
              position: relative;
              overflow: hidden; }
              .POPUPS_WRAPPER > div {
                /* page */
                margin: 0 auto; }

            .auto-generated-link {
              color: inherit; }

            .warmup .hidden-on-warmup {
              visibility: hidden; }

            html.device-phone body {
              overflow-y: auto; }

            html.device-mobile-optimized.device-android {
              margin-bottom: 1px; }

            html.device-mobile-optimized.blockSiteScrolling > body {
              position: fixed;
              width: 100%; }

            html.device-mobile-optimized.media-zoom-mode > body {
              touch-action: manipulation; }
              html.device-mobile-optimized.media-zoom-mode > body > #SITE_CONTAINER {
                height: 100%;
                overflow: hidden; }
                html.device-mobile-optimized.media-zoom-mode > body > #SITE_CONTAINER > .noop {
                  height: 100%; }
                  html.device-mobile-optimized.media-zoom-mode > body > #SITE_CONTAINER > .noop > .siteAspectsContainer {
                    height: 100%;
                    z-index: 1005; }

            .siteAspectsContainer {
              position: absolute;
              top: 0;
              margin: 0 auto;
              left: 0;
              right: 0; }

            body.device-mobile-optimized {
              overflow-x: hidden;
              overflow-y: scroll; }
              body.device-mobile-optimized.qa-mode {
                overflow-y: auto; }
              body.device-mobile-optimized #SITE_CONTAINER {
                width: 320px;
                overflow-x: visible;
                margin: 0 auto;
                position: relative; }
              body.device-mobile-optimized > * {
                max-width: 100% !important; }
              body.device-mobile-optimized .SITE_ROOT {
                overflow-x: hidden;
                overflow-y: hidden; }

            body.device-mobile-non-optimized #SITE_CONTAINER > :not(.mobile-non-optimized-overflow) .SITE_ROOT {
              overflow-x: hidden;
              overflow-y: auto; }

            body.device-mobile-non-optimized.fullScreenMode {
              background-color: #5f6360; }
              body.device-mobile-non-optimized.fullScreenMode .SITE_ROOT,
              body.device-mobile-non-optimized.fullScreenMode #SITE_BACKGROUND,
              body.device-mobile-non-optimized.fullScreenMode #MOBILE_ACTIONS_MENU {
                visibility: hidden; }

            body.fullScreenMode {
              overflow-x: hidden !important;
              overflow-y: hidden !important; }
              body.fullScreenMode.device-mobile-optimized #TINY_MENU {
                opacity: 0;
                pointer-events: none; }

            body.fullScreenMode-scrollable.device-mobile-optimized {
              overflow-x: hidden !important;
              overflow-y: auto !important; }
              body.fullScreenMode-scrollable.device-mobile-optimized .SITE_ROOT,
              body.fullScreenMode-scrollable.device-mobile-optimized #masterPage {
                overflow-x: hidden !important;
                overflow-y: hidden !important; }
              body.fullScreenMode-scrollable.device-mobile-optimized #masterPage,
              body.fullScreenMode-scrollable.device-mobile-optimized #SITE_BACKGROUND {
                height: auto !important; }

            .fullScreenOverlay {
              z-index: 1005;
              position: fixed;
              left: 0;
              top: -60px;
              right: 0;
              bottom: 0;
              display: -webkit-box;
              display: -webkit-flex;
              display: flex;
              -webkit-box-pack: center;
              -webkit-justify-content: center;
                      justify-content: center;
              overflow-y: hidden; }
              .fullScreenOverlay > .fullScreenOverlayContent {
                margin: 0 auto;
                position: absolute;
                right: 0;
                top: 60px;
                left: 0;
                bottom: 0;
                overflow: hidden;
                -webkit-transform: translateZ(0);
                        transform: translateZ(0); }

            .mobile-actions-menu-wrapper {
              z-index: 1000; }

            body[contenteditable] {
              overflow-x: auto;
              overflow-y: auto; }

            .bold {
              font-weight: bold; }

            .italic {
              font-style: italic; }

            .underline {
              text-decoration: underline; }

            .lineThrough {
              text-decoration: line-through; }

            .singleLineText {
              white-space: nowrap;
              text-overflow: ellipsis; }

            .alignLeft {
              text-align: left; }

            .alignCenter {
              text-align: center; }

            .alignRight {
              text-align: right; }

            .alignJustify {
              text-align: justify; }

            ul.font_100, ol.font_100 {
              color: #080808;
              font-family: 'Arial, Helvetica, sans-serif', serif;
              font-size: 10px;
              font-style: normal;
              font-variant: normal;
              font-weight: normal;
              margin: 0;
              text-decoration: none;
              line-height: normal;
              letter-spacing: normal; }
              ul.font_100 li, ol.font_100 li {
                margin-bottom: 12px; }

            letter {
              position: relative;
              display: inline-block; }

            word {
              display: inline-block;
              white-space: nowrap; }

            word.space,
            letter.space {
              display: inline; }

            ol.wix-list-text-align, ul.wix-list-text-align {
              list-style-position: inside; }
              ol.wix-list-text-align p, ol.wix-list-text-align h1, ol.wix-list-text-align h2, ol.wix-list-text-align h3, ol.wix-list-text-align h4, ol.wix-list-text-align h5, ol.wix-list-text-align h6, ul.wix-list-text-align p, ul.wix-list-text-align h1, ul.wix-list-text-align h2, ul.wix-list-text-align h3, ul.wix-list-text-align h4, ul.wix-list-text-align h5, ul.wix-list-text-align h6 {
                display: inline; }

            .wixapps-less-spacers-align.ltr {
              text-align: left; }

            .wixapps-less-spacers-align.center {
              text-align: center; }

            .wixapps-less-spacers-align.rtl {
              text-align: right; }

            .wixapps-less-spacers-align > div,
            .wixapps-less-spacers-align > a {
              display: inline-block !important; }

            .flex_display {
              display: -webkit-box;
              display: -webkit-flex;
              display: flex; }

            .flex_vbox {
              box-sizing: border-box;
              padding-top: 0.01em;
              padding-bottom: 0.01em; }

            a.wixAppsLink img {
              cursor: pointer; }

            .singleLine {
              white-space: nowrap;
              display: block;
              overflow: hidden;
              text-overflow: ellipsis;
              word-wrap: normal; }


             /* Dropdown Button */
            .dropbtn {
                padding: 1px;
                font-family: Georgia, Times, "Times New Roman", serif;
                font-size: 14px;
                border: none;
                cursor: pointer;
            }

            /* The container <div> - needed to position the dropdown content */
            .dropdown {
                position: relative;
                display: inline-block;
            }

            /* Dropdown Content (Hidden by Default) */
            .dropdown-content {
                display: none;
                position: absolute;
                min-width: 160px;
                font-family: Georgia, Times, "Times New Roman", serif;
                font-size: 13px;
                box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
                z-index: 1;
                background-color: #ffffff;
            }

            /* Links inside the dropdown */
            .dropdown-content a {
                color: black;
                background-color: #ffffff
                padding: 5px 5px;
                text-decoration: none;
                display: block;
            }

            /* Change color of dropdown links on hover */
            .dropdown-content a:hover {color: white; background-color: black}

            /* Show the dropdown menu on hover */
            .dropdown:hover .dropdown-content {
                display: block;
            }

            /* Change the background color of the dropdown button when the dropdown content is shown */
            .dropdown:hover .dropbtn {
                background-color: #3e8e41;
            }

            [data-z-counter] {
              z-index: 0; }

            [data-z-counter="0"] {
              z-index: auto; }

            .circle-preloader {
              -webkit-animation: semi-rotate 1s 1ms linear infinite;
                      animation: semi-rotate 1s 1ms linear infinite;
              height: 30px;
              left: 50%;
              margin-left: -15px;
              margin-top: -15px;
              overflow: hidden;
              position: absolute;
              top: 50%;
              -webkit-transform-origin: 100% 50%;
                      transform-origin: 100% 50%;
              width: 15px; }
              .circle-preloader::before {
                content: '';
                top: 0;
                left: 0;
                right: -100%;
                bottom: 0;
                border: 3px solid currentColor;
                border-color: currentColor;
                border-radius: 50%;
                position: absolute;
                -webkit-transform: rotate(-45deg);
                        transform: rotate(-45deg);
                -webkit-animation: inner-rotate 0.5s 1ms linear infinite alternate;
                        animation: inner-rotate 0.5s 1ms linear infinite alternate;
                color: #7fccf7; }
              .circle-preloader::after {
                content: '';
                top: 0;
                left: 0;
                right: -100%;
                bottom: 0;
                border: 3px solid currentColor;
                border-color: currentColor;
                border-radius: 50%;
                position: absolute;
                -webkit-transform: rotate(-45deg);
                        transform: rotate(-45deg);
                -webkit-animation: inner-rotate 0.5s 1ms linear infinite alternate;
                        animation: inner-rotate 0.5s 1ms linear infinite alternate;
                color: #3899ec;
                opacity: 0; }
              .circle-preloader.white::before {
                color: #f0f0f0; }
              .circle-preloader.white::after {
                color: #dcdcdc; }

            @-webkit-keyframes inner-rotate {
              to {
                opacity: 1;
                -webkit-transform: rotate(115deg);
                        transform: rotate(115deg); } }

            @keyframes inner-rotate {
              to {
                opacity: 1;
                -webkit-transform: rotate(115deg);
                        transform: rotate(115deg); } }

            @-webkit-keyframes semi-rotate {
              from {
                -webkit-animation-timing-function: ease-out;
                        animation-timing-function: ease-out;
                -webkit-transform: rotate(180deg);
                        transform: rotate(180deg); }
              45% {
                -webkit-transform: rotate(198deg);
                        transform: rotate(198deg); }
              55% {
                -webkit-transform: rotate(234deg);
                        transform: rotate(234deg); }
              to {
                -webkit-transform: rotate(540deg);
                        transform: rotate(540deg); } }

            @keyframes semi-rotate {
              from {
                -webkit-animation-timing-function: ease-out;
                        animation-timing-function: ease-out;
                -webkit-transform: rotate(180deg);
                        transform: rotate(180deg); }
              45% {
                -webkit-transform: rotate(198deg);
                        transform: rotate(198deg); }
              55% {
                -webkit-transform: rotate(234deg);
                        transform: rotate(234deg); }
              to {
                -webkit-transform: rotate(540deg);
                        transform: rotate(540deg); } }

            .hidden-comp-ghost-mode {
              opacity: 0.5; }

            .collapsed-comp-mode::after {
              position: absolute;
              top: 0;
              bottom: 0;
              left: 0;
              right: 0;
              content: '';
              background: -webkit-repeating-linear-gradient(135deg, #2b5672 40%, #2b5672 40%);
              background: repeating-linear-gradient(-45deg, #2b5672 40%, #2b5672 40%);
              background-size: 6px 6px;
              background-repeat: repeat; }

            .g-transparent-a:link, .g-transparent-a:visited {
              border-color: #ffffff; }

            .transitioning-comp * {
              transition: inherit !important;
              -webkit-transition: inherit !important; }

            .selectionSharerContainer {
              position: absolute;
              background-color: #ffffff;
              box-shadow: 0px 4px 10px 0px rgba(57, 86, 113, 0.24);
              width: 142px;
              height: 45px;
              border-radius: 100px;
              text-align: center; }
              .selectionSharerContainer:after {
                content: "";
                position: absolute;
                bottom: -10px;
                left: 42%;
                /*controls horizontal position */
                border-width: 10px 10px 0;
                /* vary these values to change the angle of the vertex */
                border-style: solid;
                border-color: #ffffff transparent;
                /* reduce the damage in FF3.0 */
                display: block;
                width: 0; }
              .selectionSharerContainer .selectionSharerOption {
                display: inline-block;
                cursor: pointer;
                vertical-align: top;
                padding: 13px 11px 11px 13px;
                margin: 1px;
                z-index: -1; }
              .selectionSharerContainer .selectionSharerVerticalSeparator {
                margin-top: 9px;
                margin-bottom: 18px;
                background-color: #eaf7ff;
                height: 26px;
                width: 1px;
                display: inline-block; }

            .visual-focus-on :not(.has-custom-focus):focus {
              box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.9), 0 0 1px 2px #3899EC !important; }
            /*# sourceMappingURL=viewer.css.map */</style><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="mobileLayoutUtils" src="./mysite_files/mobileLayoutUtils.js.download"></script><link rel="stylesheet" href="./mysite_files/css" id="font_googleFonts"><link rel="stylesheet" href="./mysite_files/languages.css" id="font_langauges"><meta property="og:title" content="mysite"><meta property="og:url" content="https://darinlasota.wixsite.com/mysite"><meta name="robots" content="index"><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="//www.google-analytics.com/analytics.js" src="./mysite_files/analytics.js.download"></script></head>
            <body class="">
                    <div id="SITE_CONTAINER" data-santa-render-status="CLIENT"><div class="noop" data-santa-version="1.2367.27" data-reactid=".0"><div data-reactid=".0.0"><style type="text/css" data-reactid=".0.0.$theme_fonts">.font_0 {font: normal normal bold 134px/1.4em helvetica-w01-bold,helvetica-w02-bold,helvetica-lt-w10-bold,sans-serif ;color:#FF4F59;}
            .font_1 {font: normal normal normal 16px/1.4em din-next-w01-light,din-next-w02-light,din-next-w10-light,sans-serif ;color:#646464;}
            .font_2 {font: normal normal bold 100px/1.4em helvetica-w01-bold,helvetica-w02-bold,helvetica-lt-w10-bold,sans-serif ;color:#FF4F59;}
            .font_3 {font: normal normal bold 80px/1.4em helvetica-w01-bold,helvetica-w02-bold,helvetica-lt-w10-bold,sans-serif ;color:#FF4F59;}
            .font_4 {font: normal normal bold 60px/1.4em helvetica-w01-bold,helvetica-w02-bold,helvetica-lt-w10-bold,sans-serif ;color:#FF4F59;}
            .font_5 {font: normal normal normal 24px/1.4em helvetica-w01-bold,helvetica-w02-bold,helvetica-lt-w10-bold,sans-serif ;color:#000000;}
            .font_6 {font: normal normal bold 17px/1.4em helvetica-w01-bold,helvetica-w02-bold,helvetica-lt-w10-bold,sans-serif ;color:#000000;}
            .font_7 {font: normal normal normal 24px/1.4em helvetica-w01-bold,helvetica-w02-bold,helvetica-lt-w10-bold,sans-serif ;color:#000000;}
            .font_8 {font: normal normal normal 15px/1.4em helvetica-w01-light,helvetica-w02-light,sans-serif ;color:#000000;}
            .font_9 {font: normal normal normal 13px/1.4em helvetica-w01-roman,helvetica-w02-roman,helvetica-lt-w10-roman,sans-serif ;color:#000000;}
            .font_10 {font: normal normal normal 12px/1.4em din-next-w01-light,din-next-w02-light,din-next-w10-light,sans-serif ;color:#646464;}
            </style><style type="text/css" data-reactid=".0.0.$theme_colors">.color_0 {color: #FFFFFF;}
            .backcolor_0 {background-color: #FFFFFF;}
            .color_1 {color: #FFFFFF;}
            .backcolor_1 {background-color: #FFFFFF;}
            .color_2 {color: #000000;}
            .backcolor_2 {background-color: #000000;}
            .color_3 {color: #ED1C24;}
            .backcolor_3 {background-color: #ED1C24;}
            .color_4 {color: #0088CB;}
            .backcolor_4 {background-color: #0088CB;}
            .color_5 {color: #FFCB05;}
            .backcolor_5 {background-color: #FFCB05;}
            .color_6 {color: #727272;}
            .backcolor_6 {background-color: #727272;}
            .color_7 {color: #B0B0B0;}
            .backcolor_7 {background-color: #B0B0B0;}
            .color_8 {color: #FFFFFF;}
            .backcolor_8 {background-color: #FFFFFF;}
            .color_9 {color: #727272;}
            .backcolor_9 {background-color: #727272;}
            .color_10 {color: #B0B0B0;}
            .backcolor_10 {background-color: #B0B0B0;}
            .color_11 {color: #FAFAFA;}
            .backcolor_11 {background-color: #FAFAFA;}
            .color_12 {color: #C8C8C8;}
            .backcolor_12 {background-color: #C8C8C8;}
            .color_13 {color: #969696;}
            .backcolor_13 {background-color: #969696;}
            .color_14 {color: #646464;}
            .backcolor_14 {background-color: #646464;}
            .color_15 {color: #000000;}
            .backcolor_15 {background-color: #000000;}
            .color_16 {color: #FFC4C8;}
            .backcolor_16 {background-color: #FFC4C8;}
            .color_17 {color: #FFA7AC;}
            .backcolor_17 {background-color: #FFA7AC;}
            .color_18 {color: #FF4F59;}
            .backcolor_18 {background-color: #FF4F59;}
            .color_19 {color: #AA353B;}
            .backcolor_19 {background-color: #AA353B;}
            .color_20 {color: #551A1E;}
            .backcolor_20 {background-color: #551A1E;}
            .color_21 {color: #FBD8C0;}
            .backcolor_21 {background-color: #FBD8C0;}
            .color_22 {color: #F7B383;}
            .backcolor_22 {background-color: #F7B383;}
            .color_23 {color: #B98662;}
            .backcolor_23 {background-color: #B98662;}
            .color_24 {color: #7C5A42;}
            .backcolor_24 {background-color: #7C5A42;}
            .color_25 {color: #3E2D21;}
            .backcolor_25 {background-color: #3E2D21;}
            .color_26 {color: #F0EFAF;}
            .backcolor_26 {background-color: #F0EFAF;}
            .color_27 {color: #E0DF86;}
            .backcolor_27 {background-color: #E0DF86;}
            .color_28 {color: #D1CE28;}
            .backcolor_28 {background-color: #D1CE28;}
            .color_29 {color: #8B891B;}
            .backcolor_29 {background-color: #8B891B;}
            .color_30 {color: #46450D;}
            .backcolor_30 {background-color: #46450D;}
            .color_31 {color: #B3E7CA;}
            .backcolor_31 {background-color: #B3E7CA;}
            .color_32 {color: #89D0A9;}
            .backcolor_32 {background-color: #89D0A9;}
            .color_33 {color: #3BB873;}
            .backcolor_33 {background-color: #3BB873;}
            .color_34 {color: #277B4D;}
            .backcolor_34 {background-color: #277B4D;}
            .color_35 {color: #143D26;}
            .backcolor_35 {background-color: #143D26;}
            </style><style type="text/css" data-reactid=".0.0.$fc1">.fc1screenWidthBackground {position:absolute;top:0;right:0;bottom:0;left:0;}
            .fc1[data-state~="mobileView"] {position:absolute !important;}
            .fc1[data-state~="fixedPosition"] {position:fixed !important;left:auto !important;z-index:50;}
            .fc1[data-state~="fixedPosition"].fc1_footer {top:auto;bottom:0;}
            .fc1bg {position:absolute;top:0;right:0;bottom:0;left:0;}
            .fc1inlineContent {position:absolute;top:0;right:0;bottom:0;left:0;}
            .fc1centeredContent {position:absolute;top:0;right:0;bottom:0;left:0;}</style><style type="text/css" data-reactid=".0.0.$txtNew">.txtNew {word-wrap:break-word;}
            .txtNew_override-left * {text-align:left !important;}
            .txtNew_override-right * {text-align:right !important;}
            .txtNew_override-center * {text-align:center !important;}
            .txtNew_override-justify * {text-align:justify !important;}
            .txtNew li {font-style:inherit;font-weight:inherit;line-height:inherit;letter-spacing:normal;}
            .txtNew ol,.txtNew ul {padding-left:1.3em;padding-right:0;margin-left:0.5em;margin-right:0;line-height:normal;letter-spacing:normal;}
            .txtNew ul {list-style-type:disc;}
            .txtNew ol {list-style-type:decimal;}
            .txtNew ul ul,.txtNew ol ul {list-style-type:circle;}
            .txtNew ul ul ul,.txtNew ol ul ul {list-style-type:square;}
            .txtNew ul ol ul,.txtNew ol ol ul {list-style-type:square;}
            .txtNew ul[dir="rtl"],.txtNew ol[dir="rtl"] {padding-left:0;padding-right:1.3em;margin-left:0;margin-right:0.5em;}
            .txtNew ul[dir="rtl"] ul,.txtNew ul[dir="rtl"] ol,.txtNew ol[dir="rtl"] ul,.txtNew ol[dir="rtl"] ol {padding-left:0;padding-right:1.3em;margin-left:0;margin-right:0.5em;}
            .txtNew p {margin:0;line-height:normal;letter-spacing:normal;}
            .txtNew h1 {margin:0;line-height:normal;letter-spacing:normal;}
            .txtNew h2 {margin:0;line-height:normal;letter-spacing:normal;}
            .txtNew h3 {margin:0;line-height:normal;letter-spacing:normal;}
            .txtNew h4 {margin:0;line-height:normal;letter-spacing:normal;}
            .txtNew h5 {margin:0;line-height:normal;letter-spacing:normal;}
            .txtNew h6 {margin:0;line-height:normal;letter-spacing:normal;}
            .txtNew a {color:inherit;}</style><style type="text/css" data-reactid=".0.0.$hc1">.hc1screenWidthBackground {position:absolute;top:0;right:0;bottom:0;left:0;}
            .hc1[data-state~="mobileView"] {position:absolute !important;}
            .hc1[data-state~="fixedPosition"] {position:fixed !important;left:auto !important;z-index:50;}
            .hc1[data-state~="fixedPosition"].hc1_footer {top:auto;bottom:0;}
            .hc1bg {position:absolute;top:0;right:0;bottom:0;left:0;}
            .hc1inlineContent {position:absolute;top:0;right:0;bottom:0;left:0;}
            .hc1centeredContent {position:absolute;top:0;right:0;bottom:0;left:0;}</style><style type="text/css" data-reactid=".0.0.$style-j5u60l2y">.style-j5u60l2yitemsContainer {width:calc(100% - 0px);height:calc(100% - 0px);white-space:nowrap;display:inline-block;overflow:visible;position:relative;}
            .style-j5u60l2ymoreContainer {overflow:visible;display:inherit;white-space:nowrap;width:auto;background-color:rgba(255, 255, 255, 1);border-radius:0;  }
            .style-j5u60l2ydropWrapper {z-index:99999;display:block;opacity:1;visibility:hidden;position:absolute;box-sizing:border-box;}
            .style-j5u60l2y_back {height:calc(100% - 0px - 13px);background-color:rgba(255, 255, 255, 1);position:absolute;top:0;right:0;bottom:13px;left:0;border-bottom:solid 1px rgba(52, 34, 22, 1);}
            .style-j5u60l2y[data-dropmode="dropUp"] .style-j5u60l2ydropWrapper {margin-top:0;margin-bottom:7px;}
            .style-j5u60l2yrepeaterButton {height:100%;position:relative;box-sizing:border-box;display:inline-block;cursor:pointer;}
            .style-j5u60l2yrepeaterButton[data-state~="header"] a,.style-j5u60l2yrepeaterButton[data-state~="header"] div {cursor:default !important;}
            .style-j5u60l2yrepeaterButtonlabelPad {height:13px;text-align:center;width:100%;border-top:solid 1px rgba(52, 34, 22, 1);}
            .style-j5u60l2yrepeaterButton_arr {width:0;height:0;margin:0 auto;}
            .style-j5u60l2yrepeaterButton_outer {border:solid 11px transparent;border-top-color:rgba(52, 34, 22, 1);margin-top:-1px;visibility:hidden;border-bottom-width:3px;}
            .style-j5u60l2yrepeaterButton_inner {border:solid 10px transparent;border-top-color:rgba(52, 34, 22, 1);margin-top:-14px;visibility:hidden;border-bottom-width:3px;}
            .style-j5u60l2yrepeaterButtonbg {background-color:transparent;transition: background-color 0.4s ease 0s;}
            .style-j5u60l2yrepeaterButtonlabel {display:inline-block;padding:0 calc(1px + 10px);color:#342216;font:italic normal normal 22px/1.4em 'marck script',cursive;  transition: color 0.4s ease 0s;}
            .style-j5u60l2yrepeaterButton[data-state~="drop"] {width:100%;display:block;}
            .style-j5u60l2yrepeaterButton[data-state~="drop"] .style-j5u60l2yrepeaterButtonlabel {display:inline-block;padding:0 .5em;}
            .style-j5u60l2yrepeaterButton[data-state~="drop"] .style-j5u60l2yrepeaterButtonlabelPad {display:none;}
            .style-j5u60l2yrepeaterButton[data-listposition="dropLonely"] .style-j5u60l2yrepeaterButtonbg,.style-j5u60l2yrepeaterButton[data-listposition="top"] .style-j5u60l2yrepeaterButtonbg,.style-j5u60l2yrepeaterButton[data-listposition="bottom"] .style-j5u60l2yrepeaterButtonbg {border-radius:0;}
            .style-j5u60l2yrepeaterButton[data-listposition="top"] .style-j5u60l2yrepeaterButtonbg {border-bottom-left-radius:0;border-bottom-right-radius:0;}
            .style-j5u60l2yrepeaterButton[data-listposition="bottom"] .style-j5u60l2yrepeaterButtonbg {border-top-left-radius:0;border-top-right-radius:0;}
            .style-j5u60l2yrepeaterButton[data-state~="over"] .style-j5u60l2yrepeaterButtonbg {background-color:rgba(52, 34, 22, 1);transition: background-color 0.4s ease 0s;}
            .style-j5u60l2yrepeaterButton[data-state~="over"] .style-j5u60l2yrepeaterButtonlabel {color:#FFFFFF;transition: color 0.4s ease 0s;}
            .style-j5u60l2yrepeaterButton[data-state~="selected"] .style-j5u60l2yrepeaterButtonbg {background-color:rgba(52, 34, 22, 1);transition: background-color 0.4s ease 0s;}
            .style-j5u60l2yrepeaterButton[data-state~="selected"] .style-j5u60l2yrepeaterButtonlabel {color:#FFFFFF;transition: color 0.4s ease 0s;}
            .style-j5u60l2yrepeaterButton[data-state~="selected"] .style-j5u60l2yrepeaterButton_outer,.style-j5u60l2yrepeaterButton[data-state~="selected"] .style-j5u60l2yrepeaterButton_inner {visibility:inherit;}
            .style-j5u60l2yrepeaterButton[data-state~="selected"] .style-j5u60l2yrepeaterButton_inner {border-top-color:rgba(52, 34, 22, 1);}</style><style type="text/css" data-reactid=".0.0.$pc1">.pc1screenWidthBackground {position:absolute;top:0;right:0;bottom:0;left:0;}
            .pc1[data-state~="mobileView"] {position:absolute !important;}
            .pc1[data-state~="fixedPosition"] {position:fixed !important;left:auto !important;z-index:50;}
            .pc1[data-state~="fixedPosition"].pc1_footer {top:auto;bottom:0;}
            .pc1bg {position:absolute;top:0;right:0;bottom:0;left:0;}
            .pc1inlineContent {position:absolute;top:0;right:0;bottom:0;left:0;}
            .pc1centeredContent {position:absolute;top:0;right:0;bottom:0;left:0;}</style><style type="text/css" data-reactid=".0.0.$s_VOwPageGroupSkin">.s_VOwPageGroupSkin {height:100px;width:100px;}
            .s_VOwPageGroupSkinoverlay {position:absolute;top:0;right:0;bottom:0;left:0;background-color:rgba(0, 0, 0, 0.664);}
            .s_VOwPageGroupSkininlineContent {position:absolute;top:0;right:0;bottom:0;left:0;}</style><style type="text/css" data-reactid=".0.0.$p1">.p1bg {position:absolute;top:0;right:0;bottom:0;left:0;}
            .p1[data-state~="mobileView"] .p1bg {left:10px;right:10px;}
            .p1inlineContent {position:absolute;top:0;right:0;bottom:0;left:0;}</style><style type="text/css" data-reactid=".0.0.$c1">.c1bg {border:0px solid rgba(0, 0, 0, 1);background-color:rgba(250, 250, 250, 1);border-radius:0;  }
            .c1inlineContent,.c1bg {position:absolute;top:0;right:0;bottom:0;left:0;}</style><style type="text/css" data-reactid=".0.0.$wixAds">.wixAdsmobileAd {width:100%;height:30px;position:relative;display:block;text-align:center;background-color:#313131;z-index:999;}
            .wixAdsdesktopWADBottom {position:fixed;z-index:999;width:100%;bottom:0;max-height:10vh;}
            .wixAdsdesktopWADBottomContent {width:100%;height:40px;text-align:center;background-color:#404040;border-radius:6px 6px 0 0;pointer-events:all;cursor:pointer;}
            .wixAdsdesktopWADBottomContent:hover {background-color:#222;}
            .wixAds[data-state~="facebook"] .wixAdsdesktopWADBottomContent {width:500px;margin:0 auto;}
            .wixAdsdesktopWADTop {position:fixed;z-index:999;height:26px;top:0;right:50px;overflow:hidden;background-color:#404040;border-radius:0 0 6px 6px;pointer-events:all;cursor:pointer;-webkit-transition:all .3s ease-in-out;transition:all .3s ease-in-out;}
            .wixAdsdesktopWADTop:hover {height:97px;background-color:rgba(50, 50, 50, 0.8);}
            .wixAdsdesktopWADTop:hover .wixAdsdesktopWADTopLabel {background-color:#222;}
            .wixAdsdesktopWADTopLabel {padding:6px;font-size:13px;line-height:1.3em;color:#FFF;width:100%;font-size:13px;color:#FFF;font-weight:bold;line-height:18px;text-align:justify;padding:5px 10px;}
            .wixAds[data-state~="desktop"] .wixAdsmobileAd {display:none;}
            .wixAds[data-state~="mobile"] .wixAdsdesktopWADTop {display:none;}
            .wixAds[data-state~="mobile"] .wixAdsdesktopWADBottom {display:none;}
            .wixAdsdesktopWADTopLabel .wixAds_smallMusa {display:inline-block;text-indent:-9999px;width:16px;height:16px;margin-right:5px;  background-image:url("//static.wixstatic.com/media/0da768_0c5ce9e2ffa442bea0b79b690223a939~mv2.png");background-repeat:no-repeat;background-position:0% 0%;}
            .wixAdsdesktopWADTopLabel .wixAds_smallLogo {display:inline-block;text-indent:-9999px;width:29px;height:16px;  background-image:url("//static.wixstatic.com/media/0da768_0c5ce9e2ffa442bea0b79b690223a939~mv2.png");background-repeat:no-repeat;background-position:-16px top;}
            .wixAdsdesktopWADTopContent {font-size:13px;line-height:1.3em;color:#ffffff;font-weight:bold;line-height:18px;text-align:justify;padding:5px 10px;width:100%;}
            .wixAdsdesktopWADBottomContent .wixAds_faceBanner {background-color:rgba(64, 64, 64, 1);width:500px;height:100%;margin:0 auto;border-radius:6px 6px 0 0;  padding:5px 0 0 0;}
            .wixAdsdesktopWADBottomContent .wixAds_faceBanner div {display:inline-block;height:30px;}
            .wixAdsdesktopWADBottomContent .wixAds_faceBanner .wixAds_txt {color:#fff;font-weight:bold;font-size:15px;text-align:justify;margin:-2px 10px 0 19px;}
            .wixAdsdesktopWADBottomContent .wixAds_faceBanner .wixAds_logoDot {position:static;margin:0 3px;}
            .wixAdsdesktopWADBottomContent .wixAds_faceBanner .wixAds_emphasis {font-weight:bold;position:relative;top:-6px;}
            .wixAdsdesktopWADTopContent .wixAds_spacer {line-height:26px;}
            .wixAdsdesktopWADTopContent .wixAds_emphasis {color:#ffcc00;}
            .wixAdsdesktopWADTopContent .wixAds_cap {font-size:16px;line-height:1.3em;text-transform:uppercase;}
            .wixAdsdesktopWADTopContent .wixAds_face {display:block;line-height:18px;text-align:justify;padding:0 20px;width:120px;}
            .wixAdsdesktopWADBottomContent .wixAds_adFootBox {height:40px;width:100%;text-align:center;}
            .wixAdsdesktopWADBottomContent .wixAds_siteBanner {background-color:rgba(64, 64, 64, 1);border-radius:6px 6px 0 0;  width:100%;height:100%;text-align:center;}
            .wixAdsdesktopWADBottomContent:hover .wixAds_siteBanner {background-color:#222;}
            .wixAdsdesktopWADBottomContent .wixAds_siteBanner .wixAds_wrapper {padding:5px 0;}
            .wixAdsdesktopWADBottomContent .wixAds_siteBanner .wixAds_wrapper div {display:inline-block;height:30px;}
            .wixAdsdesktopWADBottomContent .wixAds_bigMusa {text-indent:-9999px;width:36px;  background-image:url("//static.wixstatic.com/media/0da768_0c5ce9e2ffa442bea0b79b690223a939~mv2.png");background-repeat:no-repeat;background-position:left bottom;position:relative;top:-19px;}
            .wixAdsdesktopWADBottomContent.wixAds_nativeAndroid .wixAds_bigMusa {overflow:hidden;}
            .wixAdsdesktopWADBottomContent .wixAds_logoDot {text-indent:-9999px;width:39px;height:15px;position:relative;top:-4px;margin:0 5px;  background-image:url("//static.wixstatic.com/media/0da768_0c5ce9e2ffa442bea0b79b690223a939~mv2.png");background-repeat:no-repeat;background-position:right -17px;}
            .wixAdsdesktopWADBottomContent .wixAds_emphasis {color:#ffcc00;font-size:16px;text-transform:uppercase;}
            .wixAdsdesktopWADBottomContent .wixAds_txt {color:#fff;font-weight:bold;font-size:15px;}
            .wixAdsdesktopWADBottomContent .wixAds_siteBanner .wixAds_txt {line-height:47px;}@media (orientation: landscape){.wixAdsmobileAd {display:none;}}
            @media (orientation: landscape){.wixAds_wixAds[data-state~="mobile"] {display:none;}}</style><style type="text/css" data-reactid=".0.0.$deadComp">.deadComp {background:transparent;}</style><style type="text/css" data-reactid=".0.0.$siteBackground">.siteBackground {width:100%;position:absolute;}
            .siteBackgroundbgBeforeTransition {position:absolute;top:0;}
            .siteBackgroundbgAfterTransition {position:absolute;top:0;}</style><style type="text/css" data-reactid=".0.0.$loginDialog">.loginDialog {position:fixed;width:100%;height:100%;z-index:99;font-family:Arial, sans-serif;font-size:1em;color:#9C9C9C;}
            .loginDialogblockingLayer {background-color:rgba(85, 85, 85, 0.75);position:fixed;top:0;right:0;bottom:0;left:0;visibility:visible;zoom:1;overflow:auto;}
            .loginDialogdialog {background-color:rgba(170, 170, 170, 0.7);width:455px;position:fixed;padding:20px;}
            .loginDialog_wrapper {background-color:rgba(255, 255, 255, 1);padding:45px 40px 0 40px;}
            .loginDialogxButton {position:absolute;top:-14px;right:-14px;cursor:pointer;background:transparent url(https://static.parastorage.com/services/skins/2.1229.72/images/wysiwyg/core/themes/base/viewer_login_sprite.png) no-repeat right top;height:30px;width:30px;}
            .loginDialogxButton:hover {background-position:right -80px;}
            .loginDialogheader {padding-bottom:25px;line-height:30px;}
            .loginDialogfavIcon {float:left;margin:7px 7px 0 0;width:16px;height:16px;}
            .loginDialogtitle {font-size:20px;font-weight:bold;color:#555555;}
            .loginDialog[data-state~="mobile"] {position:absolute;width:100%;height:100%;z-index:99;font-family:Arial, sans-serif;font-size:1em;color:#9C9C9C;top:0;}
            .loginDialog[data-state~="mobile"] .loginDialogheader {padding-bottom:10px;line-height:30px;}
            .loginDialog[data-state~="mobile"] .loginDialogfavIcon {display:none;}
            .loginDialog[data-state~="mobile"] .loginDialogtitle {font-size:14px;}
            .loginDialog[data-state~="mobile"] .loginDialogdialog {width:260px;padding:10px;position:absolute;}
            .loginDialog[data-state~="mobile"] .loginDialog_footer {margin-top:0;padding-bottom:10px;}
            .loginDialog[data-state~="mobile"] .loginDialogcancel {font-size:14px;line-height:30px;}
            .loginDialog[data-state~="mobile"] .loginDialog_wrapper {padding:14px 12px 0 12px;}
            .loginDialog[data-state~="mobile"] .loginDialogsubmitButton {height:30px;width:100px;font-size:14px;}
            .loginDialog_forgot {text-align:left;font-size:12px;}
            .loginDialog_forgot a {color:#0198ff;border-bottom:1px solid #0198ff;}
            .loginDialog_forgot a:hover {color:#0044ff;border-bottom:1px solid #0044ff;}
            .loginDialog_error {font-size:12px;color:#d74401;text-align:right;}
            .loginDialog_footer {width:100%;margin-top:27px;padding-bottom:40px;}
            .loginDialogcancel {color:#9C9C9C;font-size:18px;text-decoration:underline;line-height:36px;}
            .loginDialogcancel:hover {color:#9c3c3c;}
            .loginDialogpasswordInput label {font-size:14px;}
            .loginDialogpasswordInput label[data-type="password"] {font-size:14px;line-height:30px;height:30px;}
            .loginDialogsubmitButton {float:right;cursor:pointer;border:solid 2px #0064a8;height:36px;width:143px;background:transparent url(https://static.parastorage.com/services/skins/2.1229.72/images/wysiwyg/core/themes/base/viewer_login_sprite.png) repeat-x right -252px;color:#ffffff;font-size:24px;font-weight:bold;box-shadow:0 1px 3px rgba(0, 0, 0, 0.5);}
            .loginDialogsubmitButton:hover {background-position:right -352px;border-color:#004286;}
            .loginDialog[data-state="normal"] .loginDialogerror {display:none;}
            .loginDialog[data-state="error"] .loginDialogerror {display:block;font-size:12px;color:#d74401;text-align:right;}
            .loginDialog[data-state="error"] .loginDialogpasswordInput {border-color:#d74401;}
            .loginDialogpasswordInput {font-size:1em;}
            .loginDialogpasswordInput label {float:none;font-size:17px;line-height:25px;color:#585858;}
            .loginDialogpasswordInput[data-state~="mobile"] label {float:none;font-size:14px;line-height:20px;color:#585858;}
            .loginDialogpasswordInputinput {padding:0 15px;width:100%;height:42px;font-size:19px;line-height:42px;color:#0198ff;margin:0 -3px;background:transparent url(https://static.parastorage.com/services/skins/2.1229.72/images/wysiwyg/core/themes/base/viewer_login_sprite.png) repeat-x right -170px;border:solid 1px #a1a1a1;box-sizing:border-box;}
            .loginDialogpasswordInput[data-state~="mobile"] .loginDialogpasswordInputinput {padding:0 15px;width:100%;height:30px;font-size:14px;line-height:30px;color:#0198ff;margin:0 -3px;background:transparent url(https://static.parastorage.com/services/skins/2.1229.72/images/wysiwyg/core/themes/base/viewer_login_sprite.png) repeat-x right -170px;border:solid 1px #a1a1a1;box-sizing:border-box;}
            .loginDialogpasswordInputinput[data-type="password"] {font-size:38px;}
            .loginDialogpasswordInput[data-state~="mobile"] .loginDialogpasswordInputinput[data-type="password"] {font-size:14px;}
            .loginDialogpasswordInputerrorMessage {display:block;font-size:12px;color:#d74401;text-align:right;height:15px;}
            .loginDialogpasswordInput:not([data-state~="invalid"]) .loginDialogpasswordInputerrorMessage {visibility:hidden;}
            .loginDialogpasswordInput[data-state~="invalid"] .loginDialogpasswordInputerrorMessage {visibility:visible;}
            .loginDialogpasswordInput[data-state~="invalid"] input {border-color:#d74401;}
            .loginDialogpasswordInput[data-state~="invalid"] .loginDialogpasswordInputinput {border-color:red;}</style><style type="text/css" data-reactid=".0.0.$strc1">.strc1inlineContent {position:absolute;top:0;right:0;bottom:0;left:0;}</style><style type="text/css" data-reactid=".0.0.$testStyle">.testStyles {position:absolute; display: none; z-index: 2}</style><div class="testStyles" data-reactid=".0.0.g"></div><style type="text/css" data-reactid=".0.0.$uploadedFonts"></style><div style="overflow:hidden;visibility:hidden;max-height:0;max-width:0;position:absolute;" data-reactid=".0.0.$fontsLoader"><style data-reactid=".0.0.$fontsLoader.0">.font-ruler-content::after {content:"@#$%%^&*~IAO"}</style></div></div><div id="SITE_BACKGROUND" class="siteBackground" style="position: absolute; top: 0px; height: 100%; width: 1583px;" data-reactid=".0.$SITE_BACKGROUND"><div id="SITE_BACKGROUND_previous_noPrev" class="siteBackgroundprevious" data-reactid=".0.$SITE_BACKGROUND.$noPrevscrollpreview" style="width: 100%; height: 100%;"><div id="SITE_BACKGROUNDpreviousImage" class="siteBackgroundpreviousImage" data-reactid=".0.$SITE_BACKGROUND.$noPrevscrollpreview.$previousImage"></div><div id="SITE_BACKGROUNDpreviousVideo" class="siteBackgroundpreviousVideo" data-reactid=".0.$SITE_BACKGROUND.$noPrevscrollpreview.$previousVideo"></div><div id="SITE_BACKGROUND_previousOverlay_noPrev" class="siteBackgroundpreviousOverlay" data-reactid=".0.$SITE_BACKGROUND.$noPrevscrollpreview.$previousOverlay"></div></div><div id="SITE_BACKGROUND_current_v8mea_j4851v12_bg" style="top: 0px; background-color: rgb(250, 250, 250); position: fixed; width: 100%; height: 100%;" data-position="fixed" class="siteBackgroundcurrent" data-reactid=".0.$SITE_BACKGROUND.$v8mea_j4851v12_bgfixedpreview"><div id="SITE_BACKGROUND_currentImage_v8mea_j4851v12_bg" style="position: absolute; top: 0px; width: 100%; background-size: cover; background-position: center center; background-repeat: no-repeat; height: 100%; background-image: url(&quot;https://static.wixstatic.com/media/759645_65f72cdbd0eb41ef8deb83ad44c8589a~mv2.png/v1/fill/w_1550,h_1089,al_c/759645_65f72cdbd0eb41ef8deb83ad44c8589a~mv2.png&quot;);" data-type="bgimage" data-height="100%" class="siteBackgroundcurrentImage" data-reactid=".0.$SITE_BACKGROUND.$v8mea_j4851v12_bgfixedpreview.$currentImage" data-image-css="{&quot;backgroundSize&quot;:&quot;cover&quot;,&quot;backgroundPosition&quot;:&quot;center center&quot;,&quot;backgroundRepeat&quot;:&quot;no-repeat&quot;,&quot;height&quot;:&quot;100%&quot;}"></div><div id="SITE_BACKGROUNDcurrentVideo" class="siteBackgroundcurrentVideo" data-reactid=".0.$SITE_BACKGROUND.$v8mea_j4851v12_bgfixedpreview.$currentVideo"></div><div id="SITE_BACKGROUND_currentOverlay_v8mea_j4851v12_bg" style="position:absolute;top:0;width:100%;height:100%;" class="siteBackgroundcurrentOverlay" data-reactid=".0.$SITE_BACKGROUND.$v8mea_j4851v12_bgfixedpreview.$currentOverlay"></div></div></div><div class="SITE_ROOT" id="SITE_ROOT" style="width:980px;padding-bottom:40px;" data-reactid=".0.$SITE_ROOT"><div id="masterPage" style="width: 980px; position: static; top: 0px; height: 100%; min-height:1134px;" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot"><footer style="width: 980px; position:absolute; left: 0px; height: 115px; bottom: 0px; padding: 1px;" class="fc1_footer fc1" data-state=" " id="SITE_FOOTER" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_FOOTER"><div id="SITE_FOOTERscreenWidthBackground" class="fc1screenWidthBackground" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_FOOTER.$screenWidthBackground" style="width: 1583px; left: -302px;"></div><div id="SITE_FOOTERcenteredContent" class="fc1centeredContent" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_FOOTER.$centeredContent"><div id="SITE_FOOTERbg" class="fc1bg" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_FOOTER.$centeredContent.$bg"></div><div id="SITE_FOOTERinlineContent" class="fc1inlineContent" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_FOOTER.$centeredContent.$inlineContent"><div style="left: 0px; width: 980px; position: absolute; top: 102px;" class="txtNew" id="comp-j5wlu1nx" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_FOOTER.$centeredContent.$inlineContent.$comp-j5wlu1nx"><p class="font_8" style="text-align:center; font-size:10px;"><span style="font-size:10px;"><span style="text-shadow:#c8c8c8 1px 1px 0px, #b4b4b4 0px 2px 0px, #a0a0a0 0px 3px 0px, rgba(140, 140, 140, 0.498039) 0px 4px 0px, #787878 0px 0px 0px, rgba(0, 0, 0, 0.498039) 0px 5px 10px;"><span style="color:#FFFFFF;"><span style="font-weight:bold;">CSS & Layout From <a href=https://www.wix.com><b>www.WIX.com</b></a>.</span></span></span></span></p></div></div></div></footer><header style="width: 980px; position: absolute; top: 0px; height: 127px; left: 0px;" class="hc1" data-state=" " id="SITE_HEADER" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER"><div id="SITE_HEADERscreenWidthBackground" class="hc1screenWidthBackground" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$screenWidthBackground" style="width: 1583px; left: -302px;"></div><div id="SITE_HEADERcenteredContent" class="hc1centeredContent" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent"><div id="SITE_HEADERbg" class="hc1bg" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$bg"></div><div id="SITE_HEADERinlineContent" class="hc1inlineContent" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent"><nav id="comp-j2kdbrah" data-menuborder-y="0" data-menubtn-border="0" data-ribbon-els="0" data-label-pad="13" data-ribbon-extra="0" data-drophposition="" data-dropalign="left" dir="ltr" style="left: 240px; width: 500px; position: absolute; top: 54px; height: 50px;" class="style-j5u60l2y" data-state="left notMobile" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah" data-dropmode="dropDown"><div class="style-j5u60l2y_back" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.0"></div><div style="text-align:left;" role="navigation" aria-label="Site navigation" id="comp-j2kdbrahitemsContainer" class="style-j5u60l2yitemsContainer" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer"><a style="display: inherit; color: grey; width: 72px; height: 50px; position: relative; box-sizing: border-box; overflow: visible;" role="button" tabindex="0" aria-haspopup="false" data-listposition="left" data-direction="ltr" href="https://darinlasota.wixsite.com/mysite" target="_self" class="style-j5u60l2yrepeaterButton" data-state="menu selected idle link notMobile" id="comp-j2kdbrah0" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j2oenfx4" data-original-gap-between-text-and-btn="1"><div style="text-align:left;" id="comp-j2kdbrah0bg" class="style-j5u60l2yrepeaterButtonbg" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j2oenfx4.$bg"><p style="text-align: left; line-height: 37px;" id="comp-j2kdbrah0label" class="style-j5u60l2yrepeaterButtonlabel" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j2oenfx4.$bg.$label">Home</p></div><div id="comp-j2kdbrah0labelPad" class="style-j5u60l2yrepeaterButtonlabelPad" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j2oenfx4.$labelPad"><div class="style-j5u60l2yrepeaterButton_outer style-j5u60l2yrepeaterButton_arr" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j2oenfx4.$labelPad.0"></div><div class="style-j5u60l2yrepeaterButton_inner style-j5u60l2yrepeaterButton_arr" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j2oenfx4.$labelPad.1"></div></div></a><a style="display: inherit; color: grey; width: 95px; height: 50px; position: relative; box-sizing: border-box; overflow: visible;" role="button" tabindex="0" aria-haspopup="false" data-listposition="center" data-direction="ltr" href="https://darinlasota.wixsite.com/mysite/traits" target="_self" class="style-j5u60l2yrepeaterButton" data-state="menu  idle link notMobile" id="comp-j2kdbrah1" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlny7v" data-original-gap-between-text-and-btn="1"><div style="text-align:left;" id="comp-j2kdbrah1bg" class="style-j5u60l2yrepeaterButtonbg" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlny7v.$bg"><p style="text-align: left; line-height: 37px;" id="comp-j2kdbrah1label" class="style-j5u60l2yrepeaterButtonlabel" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlny7v.$bg.$label">Abilities</p></div><div id="comp-j2kdbrah1labelPad" class="style-j5u60l2yrepeaterButtonlabelPad" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlny7v.$labelPad"><div class="style-j5u60l2yrepeaterButton_outer style-j5u60l2yrepeaterButton_arr" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlny7v.$labelPad.0"></div><div class="style-j5u60l2yrepeaterButton_inner style-j5u60l2yrepeaterButton_arr" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlny7v.$labelPad.1"></div></div></a><a style="display: inherit; color: grey; width: 86px; height: 50px; position: relative; box-sizing: border-box; overflow: visible;" role="button" tabindex="0" aria-haspopup="false" data-listposition="center" data-direction="ltr" href="https://darinlasota.wixsite.com/mysite/combat" target="_self" class="style-j5u60l2yrepeaterButton" data-state="menu  idle link notMobile" id="comp-j2kdbrah2" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlohbv1" data-original-gap-between-text-and-btn="1"><div style="text-align:left;" id="comp-j2kdbrah2bg" class="style-j5u60l2yrepeaterButtonbg" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlohbv1.$bg"><p style="text-align: left; line-height: 37px;" id="comp-j2kdbrah2label" class="style-j5u60l2yrepeaterButtonlabel" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlohbv1.$bg.$label">Combat</p></div><div id="comp-j2kdbrah2labelPad" class="style-j5u60l2yrepeaterButtonlabelPad" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlohbv1.$labelPad"><div class="style-j5u60l2yrepeaterButton_outer style-j5u60l2yrepeaterButton_arr" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlohbv1.$labelPad.0"></div><div class="style-j5u60l2yrepeaterButton_inner style-j5u60l2yrepeaterButton_arr" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlohbv1.$labelPad.1"></div></div></a><a style="display: inherit; color: grey; width: 74px; height: 50px; position: relative; box-sizing: border-box; overflow: visible;" role="button" tabindex="0" aria-haspopup="false" data-listposition="center" data-direction="ltr" href="https://darinlasota.wixsite.com/mysite/equipment-inventory" target="_self" class="style-j5u60l2yrepeaterButton" data-state="menu  idle link notMobile" id="comp-j2kdbrah3" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlop6b" data-original-gap-between-text-and-btn="1"><div style="text-align:left;" id="comp-j2kdbrah3bg" class="style-j5u60l2yrepeaterButtonbg" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlop6b.$bg"><p style="text-align: left; line-height: 37px;" id="comp-j2kdbrah3label" class="style-j5u60l2yrepeaterButtonlabel" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlop6b.$bg.$label">Items</p></div><div id="comp-j2kdbrah3labelPad" class="style-j5u60l2yrepeaterButtonlabelPad" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlop6b.$labelPad"><div class="style-j5u60l2yrepeaterButton_outer style-j5u60l2yrepeaterButton_arr" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlop6b.$labelPad.0"></div><div class="style-j5u60l2yrepeaterButton_inner style-j5u60l2yrepeaterButton_arr" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlop6b.$labelPad.1"></div></div></a><a style="display: inherit; color: grey; width: 84px; height: 50px; position: relative; box-sizing: border-box; overflow: visible;" role="button" tabindex="0" aria-haspopup="false" data-listposition="center" data-direction="ltr" href="https://darinlasota.wixsite.com/mysite/appearance-background" target="_self" class="style-j5u60l2yrepeaterButton" data-state="menu  idle link notMobile" id="comp-j2kdbrah4" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlozy9" data-original-gap-between-text-and-btn="0"><div style="text-align:left;" id="comp-j2kdbrah4bg" class="style-j5u60l2yrepeaterButtonbg" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlozy9.$bg"><p style="text-align: left; line-height: 37px;" id="comp-j2kdbrah4label" class="style-j5u60l2yrepeaterButtonlabel" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlozy9.$bg.$label">Persona</p></div><div id="comp-j2kdbrah4labelPad" class="style-j5u60l2yrepeaterButtonlabelPad" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlozy9.$labelPad"><div class="style-j5u60l2yrepeaterButton_outer style-j5u60l2yrepeaterButton_arr" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlozy9.$labelPad.0"></div><div class="style-j5u60l2yrepeaterButton_inner style-j5u60l2yrepeaterButton_arr" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlozy9.$labelPad.1"></div></div></a><a style="display: inherit; color: grey; width: 67px; height: 50px; position: relative; box-sizing: border-box; overflow: visible;" role="button" tabindex="0" aria-haspopup="false" data-listposition="center" data-direction="ltr" href="https://darinlasota.wixsite.com/mysite/notes" target="_self" class="style-j5u60l2yrepeaterButton" data-state="menu  idle link notMobile" id="comp-j2kdbrah5" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlpbvh" data-original-gap-between-text-and-btn="0"><div style="text-align:left;" id="comp-j2kdbrah5bg" class="style-j5u60l2yrepeaterButtonbg" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlpbvh.$bg"><p style="text-align: left; line-height: 37px;" id="comp-j2kdbrah5label" class="style-j5u60l2yrepeaterButtonlabel" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlpbvh.$bg.$label">Notes</p></div><div id="comp-j2kdbrah5labelPad" class="style-j5u60l2yrepeaterButtonlabelPad" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlpbvh.$labelPad"><div class="style-j5u60l2yrepeaterButton_outer style-j5u60l2yrepeaterButton_arr" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlpbvh.$labelPad.0"></div><div class="style-j5u60l2yrepeaterButton_inner style-j5u60l2yrepeaterButton_arr" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$dataItem-j5wlpbvh.$labelPad.1"></div></div></a><a style="display: inline-block; color: grey; width: 76px; box-sizing: border-box; height: 0px; overflow: hidden; position: absolute;" role="button" tabindex="0" aria-haspopup="true" data-listposition="center" class="style-j5u60l2yrepeaterButton" data-state="menu  idle header notMobile" id="comp-j2kdbrah__more__" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$__more__" data-original-gap-between-text-and-btn="1"><div style="text-align:left;" id="comp-j2kdbrah__more__bg" class="style-j5u60l2yrepeaterButtonbg" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$__more__.$bg"><p style="text-align: left; line-height: 37px;" id="comp-j2kdbrah__more__label" class="style-j5u60l2yrepeaterButtonlabel" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$__more__.$bg.$label">More</p></div><div id="comp-j2kdbrah__more__labelPad" class="style-j5u60l2yrepeaterButtonlabelPad" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$__more__.$labelPad"><div class="style-j5u60l2yrepeaterButton_outer style-j5u60l2yrepeaterButton_arr" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$__more__.$labelPad.0"></div><div class="style-j5u60l2yrepeaterButton_inner style-j5u60l2yrepeaterButton_arr" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$itemsContainer.$__more__.$labelPad.1"></div></div></a></div><div id="comp-j2kdbrahmoreButton" class="style-j5u60l2ymoreButton" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$moreButton"></div><div style="visibility:hidden;" data-drophposition="" data-dropalign="left" role="navigation" id="comp-j2kdbrahdropWrapper" class="style-j5u60l2ydropWrapper" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$dropWrapper"><div style="visibility:hidden;" id="subMenuContainer" class="style-j5u60l2ymoreContainer" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$SITE_HEADER.$centeredContent.$inlineContent.$comp-j2kdbrah.$dropWrapper.$moreContainer"></div></div></nav></div></div></header><div style="width: 980px; position: absolute; top: 127px; height: 96px; left: 0px;" class="pc1" data-state="" id="PAGES_CONTAINER" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$PAGES_CONTAINER"><div id="PAGES_CONTAINERscreenWidthBackground" class="pc1screenWidthBackground" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$PAGES_CONTAINER.$screenWidthBackground" style="width: 1583px; left: -302px;"></div><div id="PAGES_CONTAINERcenteredContent" class="pc1centeredContent" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$PAGES_CONTAINER.$centeredContent"><div id="PAGES_CONTAINERbg" class="pc1bg" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$PAGES_CONTAINER.$centeredContent.$bg"></div><div id="PAGES_CONTAINERinlineContent" class="pc1inlineContent" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$PAGES_CONTAINER.$centeredContent.$inlineContent"><div style="left: 0px; width: 980px; position: absolute; top: 0px; height: 896px;" class="s_VOwPageGroupSkin" id="SITE_PAGES" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$PAGES_CONTAINER.$centeredContent.$inlineContent.$SITE_PAGES"><div style="left: 0px; width: 980px; position: absolute; top: 0px; height: 896px;" class="p1" id="v8mea" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$PAGES_CONTAINER.$centeredContent.$inlineContent.$SITE_PAGES.$v8mea_DESKTOP"><div id="v8meabg" class="p1bg" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$PAGES_CONTAINER.$centeredContent.$inlineContent.$SITE_PAGES.$v8mea_DESKTOP.$bg"></div><div id="v8meainlineContent" class="p1inlineContent" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$PAGES_CONTAINER.$centeredContent.$inlineContent.$SITE_PAGES.$v8mea_DESKTOP.$inlineContent"><div style="left: 0px; width: 981px; position: absolute; top: 0px; height: 100%;" class="c1" id="comp-j5u5n6rx" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$PAGES_CONTAINER.$centeredContent.$inlineContent.$SITE_PAGES.$v8mea_DESKTOP.$inlineContent.$comp-j5u5n6rx"><div id="comp-j5u5n6rxbg" class="c1bg" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$PAGES_CONTAINER.$centeredContent.$inlineContent.$SITE_PAGES.$v8mea_DESKTOP.$inlineContent.$comp-j5u5n6rx.$bg"></div><div id="comp-j5u5n6rxinlineContent" class="c1inlineContent" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$PAGES_CONTAINER.$centeredContent.$inlineContent.$SITE_PAGES.$v8mea_DESKTOP.$inlineContent.$comp-j5u5n6rx.$inlineContent"><div style="left: 10px; width: 961px; position: absolute; top: 8px; height: 90%; overflow:auto;" class="txtNew" id="comp-j5v8mnp2" data-reactid=".0.$SITE_ROOT.$desktop_siteRoot.$PAGES_CONTAINER.$centeredContent.$inlineContent.$SITE_PAGES.$v8mea_DESKTOP.$inlineContent.$comp-j5u5n6rx.$inlineContent.$comp-j5v8mnp2">
        '''
