package dev.kitorik.jai.mixin;

import net.minecraft.client.gui.screen.ingame.BookScreen;
import net.minecraft.text.Style;
import net.minecraft.text.Text;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.gen.Accessor;
import org.spongepowered.asm.mixin.gen.Invoker;

/**
 * Доступ к внутренностям BookScreen, чтобы найти кнопку «ПРИНЯТЬ»
 * и выполнить её click-event.
 */
@Mixin(BookScreen.class)
public interface BookScreenMixin {
    /** Текст текущей страницы (в Yarn: pageContent). */
    @Accessor("pageContent")
    Text jai$getPageContent();

    /** Приватный обработчик клика по тексту. */
    @Invoker("handleComponentClick")
    boolean jai$handleComponentClick(Style style);
}
