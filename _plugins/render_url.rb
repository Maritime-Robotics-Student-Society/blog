module Jekyll
    module RenderUrlFilter
        def render_url(input)
            if input.start_with?('http')
                return "#{input}"
            else
                @site_url = @context.registers[:site].config["url"]
                return "#{@site_url}#{input}"
            end
        end
    end
end

Liquid::Template.register_filter(Jekyll::RenderUrlFilter)
