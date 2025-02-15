import { diskStorage } from 'multer';
import { extname } from 'path';

const localDiskStorage = diskStorage({
  destination: './uploads', // Save files to 'uploads' folder
  filename: (req, file, callback) => {
    const uniqueSuffix = `${Date.now()}-${Math.round(Math.random() * 1e9)}`;
    callback(null, `${file.fieldname}-${uniqueSuffix}${extname(file.originalname)}`);
  },
});

export {localDiskStorage};