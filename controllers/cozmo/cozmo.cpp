#include <webots/Robot.hpp>
#include <webots/Camera.hpp>
#include <webots/Display.hpp>
#include <webots/ImageRef.hpp>
#include <webots/LED.hpp>
#include <webots/Motor.hpp>
#include <webots/Speaker.hpp>
#include <webots/Supervisor.hpp>

#include <limits>

using namespace webots;

int main(int argc, char **argv) {
  Supervisor* robot = new Supervisor();
  printf("***\nHello, please turn the sound on in Webots and on your computer if you would like to listen to my Christmas song ;)\n");
  int timeStep = robot->getBasicTimeStep();
  webots::Motor* leftMotor  = robot->getMotor("LeftWheelMotor");
  webots::Motor* rightMotor = robot->getMotor("RightWheelMotor");

  webots::Motor* liftMotor = robot->getMotor("LiftMotor");
  webots::Motor* headMotor = robot->getMotor("HeadMotor");

  webots::Speaker* headSpeaker = robot->getSpeaker("HeadSpeaker");
  webots::Camera *headCamera = robot->getCamera("HeadCamera");
  webots::Display *display = robot->getDisplay("face_display");
  webots::ImageRef *awe = display->imageLoad("cozmo-awe.png");
  webots::ImageRef *surprised = display->imageLoad("cozmo-surprised.png");
  webots::ImageRef *happy = display->imageLoad("cozmo-happy.png");
  webots::LED *ledHealth[3];
  ledHealth[0] = robot->getLED("ledHealth0");
  ledHealth[1] = robot->getLED("ledHealth1");
  ledHealth[2] = robot->getLED("ledHealth2");
  webots::LED *ledDirLeft = robot->getLED("ledDirLeft");
  webots::LED *ledDirRight = robot->getLED("ledDirRight");
  headCamera->enable(timeStep * 8);
  display->imagePaste(awe, 0, 0, false);
  // Make motors velocity-controlled
  leftMotor ->setPosition(std::numeric_limits<double>::infinity());
  rightMotor->setPosition(std::numeric_limits<double>::infinity());

  headMotor->setPosition(0);
  
  // Set initial velocities
  leftMotor ->setVelocity(0);
  rightMotor->setVelocity(0);
  ledHealth[0]->set(0xff0000);
  // Main control loop

  robot->step(timeStep * 100);
  liftMotor->setPosition(0);
  
  leftMotor ->setVelocity(0.01);
  rightMotor->setVelocity(0.01);
  robot->step(timeStep * 90);
  leftMotor ->setVelocity(-0.01);
  rightMotor->setVelocity(-0.01);
  robot->step(timeStep * 150);
  
  leftMotor ->setVelocity(0.1);
  rightMotor->setVelocity(0.1);
  robot->step(timeStep * 180);
  leftMotor ->setVelocity(0);
  rightMotor->setVelocity(0);
  robot->step(timeStep * 150);
  
  leftMotor ->setVelocity(0.12);
  rightMotor->setVelocity(-0.12);
  robot->step(timeStep * 147);
  display->imagePaste(happy, 0, 0, false);
  leftMotor ->setVelocity(0);
  rightMotor->setVelocity(0);
  robot->step(timeStep * 100);
  leftMotor ->setVelocity(-0.1);
  rightMotor->setVelocity(-0.1);
  robot->step(timeStep * 370);
  leftMotor ->setVelocity(0);
  rightMotor->setVelocity(0);
  robot->step(timeStep * 80);
  leftMotor ->setVelocity(0.05);
  rightMotor->setVelocity(-0.05);
  robot->step(timeStep * 500);
  leftMotor ->setVelocity(0);
  rightMotor->setVelocity(0);
  headMotor->setPosition(-0.2);
  liftMotor->setPosition(0.2);
  robot->step(timeStep * 30);
  liftMotor->setPosition(0);
  headMotor->setPosition(0);

  int stepCounter = 2000, ledAnimation = 0;
  while (robot->step(timeStep) != -1) {
    if (stepCounter >= 2000) {
      if (headSpeaker)
        webots::Speaker::playSound(headSpeaker, headSpeaker, "cozmo_christmas_song.wav", 0.8, 1.0, 0, false);
      stepCounter = 0;
    }
    if (stepCounter % 200 == 0 && stepCounter < 1000) {
      ledDirLeft->set(0x000000);
      ledDirRight->set(0xff0000);
      display->imagePaste(happy, 0, 0, false);
      headMotor->setPosition(-0.1);
      leftMotor ->setVelocity(0.05);
      rightMotor->setVelocity(-0.05);
    }
    if ((stepCounter + 100) % 200 == 0 && stepCounter < 1000) {
      ledDirLeft->set(0xff0000);
      ledDirRight->set(0x000000);
      display->imagePaste(awe, 0, 0, false);
      headMotor->setPosition(0.1);
      leftMotor ->setVelocity(-0.05);
      rightMotor->setVelocity(0.05);
    }
    if (stepCounter % 50 == 0) {
      ledAnimation++;
      switch(ledAnimation % 4) {
      case 0:
        ledHealth[0]->set(0x00ff00);
        ledHealth[1]->set(0x000000);
        ledHealth[2]->set(0x000000);
        break;
      case 1:
        ledHealth[0]->set(0x000000);
        ledHealth[1]->set(0x00ff00);
        ledHealth[2]->set(0x000000);
        break;
      case 2:
        ledHealth[0]->set(0x000000);
        ledHealth[1]->set(0x000000);
        ledHealth[2]->set(0x00ff00);
        break;
      case 3:
        ledHealth[0]->set(0x000000);
        ledHealth[1]->set(0x00ff00);
        ledHealth[2]->set(0x000000);
        break;
      }
    }
    if (stepCounter == 1000) {
      liftMotor->setPosition(0.8);
      headMotor->setPosition(0.3);
    }
    if (stepCounter == 1500) {
      ledDirLeft->set(0x000000);
      ledDirRight->set(0x000000);
      display->imagePaste(surprised, 0, 0, false);
      liftMotor->setPosition(0);
      headMotor->setPosition(0);
      leftMotor ->setVelocity(0);
      rightMotor->setVelocity(0);
    }
    ++stepCounter;
  }

  delete robot;
  return 0;
}
