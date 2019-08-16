module Jekyll
    module RenderNavigationAnchorAttributesFilter
        def render_anchor_attributes(input)
            if input.start_with?('https')
                "href=\"#{input}\" target=\"_blank\""
            else
                @site_url = @context.registers[:site].config["url"]
                "href=\"#{@site_url}#{input}\""
            end
        end
    end
end

Liquid::Template.register_filter(Jekyll::RenderNavigationAnchorAttributesFilter)
