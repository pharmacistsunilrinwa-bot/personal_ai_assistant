import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  final String baseUrl; // Set this to your ngrok URL

  ApiService({required this.baseUrl});

  Future<String> sendChatMessage(String message, List<Map<String, String>> history) async {
    final response = await http.post(
      Uri.parse('$baseUrl/chat'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'prompt': message,
        'history': history,
      }),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body)['response'];
    } else {
      throw Exception('Failed to get response from AI');
    }
  }

  Future<List<dynamic>> searchWeb(String query) async {
    final response = await http.post(
      Uri.parse('$baseUrl/search'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'query': query}),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body)['results'];
    } else {
      throw Exception('Failed to search web');
    }
  }
}
