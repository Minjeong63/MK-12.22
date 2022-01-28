import { Module } from '@nestjs/common';
import { BoardService } from './board/board.service';
import { BoardController } from './board/board.controller';
import { BoardModule } from './board/board.module';

@Module({
  imports: [BoardModule],
  controllers: [BoardController],
  providers: [BoardService],
})
export class AppModule { }
