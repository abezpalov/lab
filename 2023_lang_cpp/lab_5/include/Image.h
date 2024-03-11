#ifndef IMAGE_H
#define IMAGE_H

#include <string>
#include <vector>



// Абстрактный класс Изображение

class Image {
    public:
        Image();
        virtual ~Image() = 0;
        virtual bool open(std::string file_name) = 0;
        virtual bool save(std::string file_name) = 0;
        virtual bool close() = 0;

    protected:
        std::vector<long> binary_content;
        std::string string_content;
        std::string file_name;

    private:
};


class VectorImage: public Image {
    public:
        VectorImage();
        VectorImage(std::string string_content);
        virtual ~VectorImage();

        virtual bool open(std::string file_name);
        virtual bool save(std::string file_name);
        virtual bool close();

    protected:

    private:

};


class BinaryImage: public Image {
    public:
        BinaryImage();
        BinaryImage(std::vector<long> binary_content);
        virtual ~BinaryImage();

        virtual bool open(std::string file_name);
        virtual bool save(std::string file_name);
        virtual bool close();

    protected:

    private:

};

#endif // IMAGE_H
