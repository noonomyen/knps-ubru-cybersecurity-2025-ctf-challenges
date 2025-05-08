#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>

#define SSID "Home WiFi"
#define PSK "0912345678"

// These are mock defines to help the IDE with autocomplete and syntax checks.
// The actual values are provided by the build system during compile time.
// #define TARGET_BLINK 1
// #define TARGET_AP 1
// #define TARGET_STA 1

String get_macaddr(uint8 if_index) {
    uint8_t mac[6];
    char macStr[18] = { 0 };
    wifi_get_macaddr(if_index, mac);

    sprintf(macStr, "%02X:%02X:%02X:%02X:%02X:%02X", mac[0], mac[1], mac[2], mac[3], mac[4], mac[5]);
    return String(macStr);
}

void setup() {
    pinMode(LED_BUILTIN, OUTPUT);

    Serial.begin(115200);

    Serial.println();

    Serial.printf("SSID: %s\n", SSID);
    Serial.printf("PSK: %s\n", PSK);

    #ifdef TARGET_BLINK
        Serial.println("Target mode: BLINK");
    #endif /* TARGET_BLINK */

    #ifdef TARGET_AP
        Serial.println("Target mode: AP");
        WiFi.mode(WIFI_AP);

        uint8_t MacAddr[6] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x01};
        wifi_set_macaddr(SOFTAP_IF, MacAddr);
        delay(1000);
        Serial.printf("MAC Address: %s\n", get_macaddr(SOFTAP_IF).c_str());

        WiFi.softAP(SSID, PSK);
    #endif /* TARGET_AP */

    #ifdef TARGET_STA
        Serial.println("Target mode: STA");
        WiFi.mode(WIFI_STA);

        uint8_t MacAddr[6] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x02};
        wifi_set_macaddr(STATION_IF, MacAddr);
        delay(1000);
        Serial.printf("MAC Address: %s\n", get_macaddr(STATION_IF).c_str());

        WiFi.begin(SSID, PSK);
        WiFi.setAutoReconnect(true);
        WiFi.persistent(true);
    #endif /* TARGET_STA */
}

void loop() {
    #ifdef TARGET_BLINK
        digitalWrite(LED_BUILTIN, LOW);
        delay(500);
        digitalWrite(LED_BUILTIN, HIGH);
        delay(500);
    #endif /* TARGET_BLINK */

    #ifdef TARGET_AP
        delay(100);
    #endif /* TARGET_AP */

    #ifdef TARGET_STA
        delay(100);
        switch (WiFi.status()) {
            case WL_CONNECTED:
                digitalWrite(LED_BUILTIN, HIGH);
                break;
            default:
                digitalWrite(LED_BUILTIN, LOW);
                break;
        }
    #endif /* TARGET_STA */
}
