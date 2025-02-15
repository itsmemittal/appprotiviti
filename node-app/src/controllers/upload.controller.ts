import {
  Controller,
  Post,
  Res,
  UploadedFile,
  UseInterceptors,
} from '@nestjs/common';
import { FileInterceptor } from '@nestjs/platform-express';
import axios from 'axios';
import { Response } from 'express';
import * as FormData from 'form-data';

@Controller()
export class UploadController {
  @Post('upload')
  @UseInterceptors(FileInterceptor('file'))
  async uploadFile(
    @UploadedFile() file: Express.Multer.File,
    @Res() res: Response,
  ) {
      console.log('uploading file')
      const formData = new FormData();
      formData.append('file', file.buffer, {
        filename: file.originalname, // Set the filename
        contentType: file.mimetype, // Set the content type
      });
    const response = await axios.post(
      'http://localhost:8000/check_forge',
      formData,
      {
        headers: {...formData.getHeaders(),  },
      },
    );
    res.setHeader(
      'Content-Disposition',
      'attachment; filename=forge_check_result.json',
    );
    res.setHeader('Content-Type', 'application/json');
    res.send(response?.data);
  }
}
