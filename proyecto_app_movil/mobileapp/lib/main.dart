import 'dart:io';

import 'package:camera/camera.dart';
import 'package:flutter/material.dart';
import 'package:mobileapp/api_client.dart';
import 'package:mobileapp/camera_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.orange),
        useMaterial3: true,
      ),
      home: const MainScreen(),
    );
  }
}

class MainScreen extends StatefulWidget {
  const MainScreen({super.key});

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  String _answer = "";
  String imagePath = "";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.orange,
        title: const Text("Contador de calorías"),
      ),
      body: Center(
        child: Column(
          children: <Widget>[
            const SizedBox(
              height: 20,
            ),
            const Text(
              'Toma una foto a tu comida:',
              style: TextStyle(fontSize: 20),
            ),
            const SizedBox(
              height: 10,
            ),
            Container(
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(10),
                border: Border.all(
                  color: Colors.orange,
                  width: 2,
                ),
              ),
              child: GestureDetector(
                onTap: () => _takePicture(context),
                child: Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: imagePath.isEmpty
                        ? Image.asset(
                            "assets/camera.png",
                            width: 200,
                          )
                        : Image.file(
                            File(imagePath),
                            width: 200,
                          )),
              ),
            ),
            const SizedBox(
              height: 10,
            ),
            ElevatedButton(
              onPressed: () {
                _calculateMacronutrients();
              },
              child: const Text("Calcular Macronutrientes"),
            ),
            const SizedBox(
              height: 10,
            ),
            if (_answer.isNotEmpty) _resultsWidget(context)
          ],
        ),
      ),
    );
  }

  Widget _resultsWidget(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(8),
      width: double.infinity,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(10),
        border: Border.all(
          color: Colors.orange,
          width: 2,
        ),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            "Resultados:",
            style: TextStyle(fontWeight: FontWeight.bold),
          ),
          Text(_answer),
        ],
      ),
    );
  }

  _takePicture(BuildContext context) async {
    WidgetsFlutterBinding.ensureInitialized();

    final cameras = await availableCameras();
    final firstCamera = cameras.first;

    if (context.mounted) {
      final imagePath = await Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => TakePictureScreen(camera: firstCamera),
        ),
      );
      setState(() {
        this.imagePath = imagePath;
      });
    }
  }

  _calculateMacronutrients() {
    ApiClient().calculateNutrients(imagePath).then((value) {
      setState(() {
        _answer = value.answer;
      });
    }).catchError((error) {
      setState(() {
        _answer = "Error al calcular los macronutrientes";
      });
    });
  }
}
