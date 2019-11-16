#include <iostream>
#include <fstream>
#include <string>
#include <TApplication.h>
#include <TF1.h>
#include <TH1.h>
#include <TCanvas.h>
#include <TStyle.h>
using namespace std;
bool ReadData(char * fileName, TH1D*  myHisto){
        string file = fileName;
        ifstream InFile(file.c_str());
        if(InFile.good()==0)
                return false;

        double x;
        while(true){
                InFile >> x;
                myHisto->Fill(x);
                if(InFile.eof()==true)
                        break;
        }
        return true;
}
int main(int argc, char ** argv){
        TApplication * app = new TApplication("myApp",NULL,NULL);
        TCanvas* cnv=new TCanvas("myCanv","myCanv",0,0,1200,800);
        TH1D * histo= new TH1D("name","title",20, 0, 50);
        if(!ReadData(argv[1], histo)){
                cout << "Errore";
        }
        cnv->cd();
        histo->Draw("same");
        cnv->Modified();
        cnv->Update();
        cnv->Print("es1.png", "png");
        app->Run();

}
