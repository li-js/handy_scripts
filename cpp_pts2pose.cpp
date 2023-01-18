// Example program
#include <iostream>
#include <string>
#include <math.h>

struct Point
{
	float x;
	float y;
};

int main()
{
  std::string name;
  std::cout << "What is your name? ";
  
  std::string dir_img = "fdf";

	const float PseudoInverseFaceModel[] = {
		-0.016393604f, 0.016393604f, 0.0f, 0.0f,
		0.0f, 0.0f, -0.0067330846f, 0.019016720f,
		0.0f, 0.0f, -0.044531129f, 0.021565545f
	};


	const int N = sizeof(PseudoInverseFaceModel) / sizeof(PseudoInverseFaceModel[0]) / 3;
	float parts_x[4], parts_y[4];
	Point parts[4];

	//Copy left, right eye center and nose tip
// 	std::vector<Point> _landmarks;
	Point _landmarks[5] = {};
// 	for (int i=1; i<=5; i++) 
    _landmarks[0] = Point{0.1,0.1};
    _landmarks[1] = Point{0.52,0.12};
    _landmarks[2] = Point{0.21,0.45};
    _landmarks[3] = Point{0.16,0.86};
    _landmarks[4] = Point{0.45,0.88};
    
	    
	
	parts[0] = _landmarks[0];
	parts[1] = _landmarks[1];
	parts[2] = _landmarks[2];
	parts[3] = { (_landmarks[3].x + _landmarks[4].x) / 2, (_landmarks[3].y + _landmarks[4].y) / 2 };
	Point eye_center = { (_landmarks[0].x + _landmarks[1].x) / 2, (_landmarks[0].y + _landmarks[1].y) / 2 };

	float xmat[N];
	float ymat[N];

	for (int i = 0; i < N; i++) {
		xmat[i] = parts[i].x - eye_center.x;
		ymat[i] = parts[i].y - eye_center.y;
	}

	//
	//  Use pseudo inverse of FaceModelPos calculated off-line
	float Amat[3];
	float Bmat[3];

	for (int i = 0; i < 3; i++)
	{
		Amat[i] = 0;
		Bmat[i] = 0;
		for (int j = 0; j < 4; j++)
		{
			Amat[i] += PseudoInverseFaceModel[4 * i + j] * xmat[j];
			Bmat[i] += PseudoInverseFaceModel[4 * i + j] * ymat[j];
		}
	}
	float A00 = Amat[0];
	float A10 = Amat[1];
	float A20 = Amat[2];
	float B00 = Bmat[0];
	float B10 = Bmat[1];
	float B20 = Bmat[2];

	// Roll
	float roll_rad = -atan2(B00, A00);
	float Cr = cos(roll_rad);
	float Sr = sin(roll_rad);

	// Pitch
	float pitch_rad = atan2(Sr*A20 - Cr * B20, Cr*B10 - Sr * A10);
	float Cp = cos(pitch_rad);
	float Sp = sin(pitch_rad);

	// Yaw
	float yaw_rad = -atan2((A10 + B10)*Sp + (A20 + B20)*Cp, A00 + B00);

	// Normalize to -1 ~ 1 range
// 	float M_PI=3.14159265357;
	float roll = roll_rad / M_PI;
	float yaw = yaw_rad / M_PI;
	float pitch = pitch_rad / M_PI;

    std::cout << "yaw:"<<yaw << " pitch:"<<pitch << " roll: "<<roll<<std::endl ; 
    std::cout<<"LJS DDDDDD " << __FILE__<<":"<<__LINE__<<"   yaw:"<<yaw<<std::endl;    

 
}
