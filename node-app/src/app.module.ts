import { Module } from '@nestjs/common';
import { AppService } from './services/app.service';
import { AuthController } from './controllers/auth.controller';
import { AppController } from './controllers/app.controller';
import { UploadController } from './controllers/upload.controller';
import { MulterModule } from '@nestjs/platform-express';
import * as multer from 'multer';

@Module({
  imports: [
    MulterModule.register({
      storage: multer.memoryStorage(),
    }),
  ],
  controllers: [AppController, AuthController, UploadController],
  providers: [AppService],
})
export class AppModule {}
