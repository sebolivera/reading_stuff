var banner_clicked = 0;
function get_random(min, max)
{
    return Math.floor(min + Math.random() * max)
}
var _randX = Math.trunc(get_random(-10, 10));
var _randY = Math.trunc(get_random(-10, 10));
var big_randX = Math.trunc(get_random(-1000, 1000));
var big_randY = Math.trunc(get_random(-1000, 1000));
var _deg = get_random(-90, 90);
var old_anim = "";

$(document).ready(function()
{
    $("#darkModeSwitch").change(function()
    {
        location.href=set_color_mode_path+"?site_color_mode=dark";
    });
    $("#lightModeSwitch").change(function()
    {
        location.href=set_color_mode_path+"?site_color_mode=light";
    });
    
    $(".site-heading").on("click", function(){
        if (banner_clicked < 1)
        {   
            $(this).first().append("<h1 style='position:absolute'>STOP THAT</h1>");
            $('.masthead').animate(
                { deg: _deg },{
                duration: 250,
                step: function(now, fx) {
                    $(this).css({ transform: 'rotate(' + now + 'deg)' });
                }
            });

            old_anim = "transform: rotate(" + _deg + "deg)";
            $('.masthead').promise().done(function(){
                banner_clicked++;

            });
        }
        else if (banner_clicked == 1)
        { 
            $('.masthead').animate(
                {randX : _randX, randY : _randY},
                {
                duration: 250,
                step: function(now, fx) {
                    this.style.transform += ' translate(' + this.randX + 'px, ' + this.randY + 'px)';
                }
            });
            $('.masthead').promise().done(function(){
                banner_clicked++;
            });
        }
        else
        {
            $('.masthead').animate(
                { randX : big_randX, randY : big_randY},
                {
                duration: 250,
                step: function(now, fx) {
                    this.style.transform += ' translate(' + this.randX + 'px, ' + this.randY + 'px)';
                }
                }
            );
        }
    });
});