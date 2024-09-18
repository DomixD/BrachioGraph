BrachioGraph - the cheapest, simplest possible pen-plotter
==========================================================

`BrachioGraph <https://www.brachiograph.art/>`_ is an ultra-cheap (total cost of materials: ~€14) plotter that can be built with minimal skills.

At its heart is a Raspberry Pi Pico 2 and some relatively simple custom software, driving three servo motors.

The mechanical hardware can be built from nothing but two sticks, a pen or pencil and some glue. No tools are required.

Almost everything required can be found in a desk or kitchen drawer. The entire device can be built with no special skills in about an hour.


.. image:: docs/images/readme_combined_image.png
    :width: 100%

Raspberry Pi Pico2
------------------

.. image:: docs/images/pico2_pinout.png
    :width: 100%

.. list-table:: Wiring up the Brachiograph
   :widths: 25 25
   :header-rows: 1

   * - Servo
     - Raspberry Pi Pico2 GPIO
     - Physical Pin
   * - 5V
     - VBUS
     - 40
   * - GND
     - GND
     - 38
   * - Shoulder
     - GP 16
     - 21
   * - Elbow
     - GP17
     - 22
   * - Pen
     - GP 18
     - 24


Documentation
-------------

`Complete documentation for the project, with detailed instructions on how to build and use it <https://www.brachiograph.art/>`_
