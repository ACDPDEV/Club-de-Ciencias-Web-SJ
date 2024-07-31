import reflex as rx


def loader() -> rx.Component:
    return rx.html(
        """
        <div id="loader-container">
            <head>
                <link rel="stylesheet" href="index.css">
                <link rel="stylesheet" href="loader.css">
            </head>
            <div class="sj-container">
                <svg width="193" height="280" viewBox="0 0 193 280" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <g class="insignia">
                        <path class="Vector-1" d="M89 101H47.5V61H150V78.5H186C186 78.5 186 50.75 186 47.5C186 44.25 176.75 29.5 168 29.5C159.25 29.5 41 29.5 34 29.5C27 29.5 6.99998 49 7 56.5C7.00002 64 7 107.5 7 114.5C7 121.5 22.9999 136.5 29.5 136.5H89M134.5 101H163.5C172.25 101 186 119 186 123.5C186 128 186 176.891 186 185.821C186 194.75 163.5 212.5 154.5 212.5C145.5 212.5 47.5001 212.5 38.5 212.5C29.4999 212.5 6.99998 194.75 7 185.821C7.00002 176.891 7 154.5 7 154.5H47.5V172.5H150V136.5H134.5"/>
                        <path class="Vector-2" d="M91.5 63.5V170M91.5 27V7H132V27M132 63.5V170M91.5 215V238H56C54 238 51.5 233.5 51.5 229H7V247C6.99998 253 23.5 273.5 29 273.5H114C123 273.5 132 269 132 260.5V215"/>
                    </g>
                </svg>
            </div>
            <div class="logo-container">
                <svg width="258" height="252" viewBox="0 0 258 252" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <g class="logo">
                        <path class="Vector-1" d="M143.167 8C208.158 17.1977 248.656 68.0266 249.996 129.087C248.088 179.612 223.532 223.287 178.035 242.538C163.751 248.582 149.573 236.611 149.573 221.101V97.2653H181.911C192.809 97.2653 201.644 88.4303 201.644 77.5319V77.5319C201.644 66.6334 192.818 57.7985 181.92 57.7985C165.113 57.7985 143.625 57.7985 143.374 57.7985"/>
                        <path class="Vector-2" d="M114.859 8C49.8683 17.2055 9.37002 68.0777 8.0307 129.19C6.9827 174.646 32.8523 218.46 78.7101 240.545C93.239 247.542 108.453 235.546 108.453 219.42V97.3413H76.1326C65.2249 97.3413 56.3824 88.4988 56.3824 77.5911V77.5911C56.3824 66.6833 65.2156 57.8408 76.1233 57.8408C92.9276 57.8408 114.401 57.8408 114.652 57.8408"/>
                    </g>
                </svg>
            </div>
            <script>
                setTimeout(function() {
                    document.getElementById('loader-container').classList.add('hidden');
                }, 6000);
            </script>
        </div>
        """,
        
        position="fixed",
        
        z_index="1000",
    )