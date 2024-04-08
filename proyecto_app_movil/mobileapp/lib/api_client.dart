import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:http_parser/http_parser.dart';

const String api = "https://nutrients-assitant.fly.dev";

class ApiClient {
  Future<NutrientsResponse> calculateNutrients(String photoPath) async {
    final uri = Uri.parse("$api/query");
    final request = http.MultipartRequest('POST', uri);
    request.files.add(
      await http.MultipartFile.fromPath('photo', photoPath,
          contentType: MediaType('image', 'jpeg')),
    );

    final streamedResponse = await request.send();
    final response = await http.Response.fromStream(streamedResponse);
    if (response.statusCode == 200) {
      return NutrientsResponse.fromJson(json.decode(response.body));
    } else {
      throw Exception("Failed to calculate nutrients");
    }
  }
}

class NutrientsResponse {
  final String answer;

  NutrientsResponse({required this.answer});

  factory NutrientsResponse.fromJson(Map<String, dynamic> json) {
    return NutrientsResponse(answer: json['answer']);
  }
}
