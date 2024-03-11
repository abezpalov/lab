#include "Image.h"

#include <iostream>
#include <string>
#include <vector>

Image::Image() {
    //ctor
}

Image::~Image() {
    //dtor
}

VectorImage::VectorImage(){
    this->string_content = "";
    this->file_name = "";
}

VectorImage::VectorImage(std::string string_content){
    this->string_content = string_content;
}

VectorImage::~VectorImage() {
    //dtor
}

bool VectorImage::open(std::string file_name) {
    std::cout << "Faked open vector image: " << file_name << std::endl;
    this->file_name = file_name;
    this->string_content = "faked data";
    return true;
}

bool VectorImage::save(std::string file_name) {
    std::cout << "Faked save vector image: " << file_name << std::endl;
    this->file_name = file_name;
    return true;
}

bool VectorImage::close() {
    std::cout << "Faked close vector image: " << file_name << std::endl;
    this->file_name = "";
    this->string_content = "";
    return true;
}

BinaryImage::BinaryImage(){
    this->string_content = "";
    this->file_name = "";
}

BinaryImage::BinaryImage(std::vector<long> binary_content){
    this->binary_content = binary_content;
    std::string string_content = "";
}

BinaryImage::~BinaryImage() {
    //dtor
}

bool BinaryImage::open(std::string file_name) {
    std::cout << "Faked open binary image: " << file_name << std::endl;
    this->file_name = file_name;
    std::vector<long> loaded_data = {1, 2, 42};
    this->binary_content = loaded_data;
    return true;
}

bool BinaryImage::save(std::string file_name) {
    std::cout << "Faked save binary image: " << file_name << std::endl;
    this->file_name = file_name;
    return true;
}

bool BinaryImage::close() {
    std::cout << "Faked close binary image: " << file_name << std::endl;
    this->file_name = "";
    std::vector<long> loaded_data();
    this->string_content = "";
    return true;
}
