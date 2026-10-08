const fs = require('fs');

const mappings = {
    'carpenter': 'images/new_carpenter_icon.jpg',
    'wood-furniture-polish': 'images/new_wood_polish_icon.jpg',
    'fan-installation': 'images/new_fan_installation_icon.jpg',
    'furniture-assembly': 'images/new_carpenter_icon.jpg',
    'geyser-service': 'images/new_geyser_repair_icon.jpg',
    'ikea-furniture': 'images/new_carpenter_icon.jpg',
    'tile-grouting': 'images/new_tile_grouting_icon.jpg',
    'festival-lights': 'images/new_festival_lights_icon.jpg',
    'wall-panels': 'images/new_wall_panels_icon.jpg',
    'electrician': 'images/new_electrician_icon.jpg',
    'plumber': 'images/new_plumber_icon.jpg'
};

const placeholders = [
    'images/plumber.jpg', 
    'images/carpenter.jpg', 
    'images/renovation.jpg', 
    'images/tools.jpg', 
    'images/beauty.jpg', 
    'images/cleaning.jpg', 
    'images/electrician_icon.jpg', 
    'images/kitchen.jpg',
    'images/carpenter_icon.jpg',
    'images/bath_icon.jpg',
    'images/basin_icon.jpg',
    'images/tank_icon.jpg',
    'images/toilet_icon.jpg',
    'images/accessories_icon.jpg',
    'images/motor_icon.jpg',
    'images/drainage_icon.jpg',
    'images/leakage_icon.jpg',
    'images/grouting_icon.jpg',
    'images/consultation.jpg',
    'images/switch_icon.jpg',
    'images/fan_icon.jpg',
    'images/light_icon.jpg',
    'images/wiring_icon.jpg',
    'images/doorbell_icon.jpg',
    'images/mcb_icon.jpg',
    'images/appliances_icon.jpg',
    'images/switch-repair.png',
    'images/plug.png',
    'images/switchbox.png',
    'images/fan-repair.png',
    'images/fan-install.png',
    'images/fan-decorative.png',
    'images/exhaust-fan.png',
    'images/fan-regulator.png',
    'images/fancy-light.png',
    'images/tubelight.png',
    'images/bulb.png',
    'images/ceiling-light.png',
    'images/hanging-light.png',
    'images/chandelier.png',
    'images/internal-wiring.png',
    'images/external-wiring.png',
    'images/doorbell.png',
    'images/video-doorbell.png',
    'images/cctv.png',
    'images/mcb-repair.png',
    'images/mcb-replacement.png',
    'images/submeter.png',
    'images/home-theatre.png',
    'images/tv-installation.png',
    'images/tv-uninstallation.png',
    'images/sound-bar.png',
    'images/karban-airzone.png',
    'images/inverter.png',
    'images/stabiliser.png',
    'images/inverter-fuse.png',
    'images/inverter-servicing.png',
    'images/inverter-checkup.png',
    'images/inverter-uninstallation.png',
    'images/consultation-banner.png'
];

for (const [file, newImg] of Object.entries(mappings)) {
    if (fs.existsSync(file)) {
        let content = fs.readFileSync(file, 'utf8');
        
        // Fix the onerror src
        content = content.replace(/onerror="this\.src='[^']+'"/g, `onerror="this.src='${newImg}'"`);
        
        // Fix placeholders used directly in src
        for (const placeholder of placeholders) {
            const regex = new RegExp(`src="${placeholder}"`, 'g');
            content = content.replace(regex, `src="${newImg}"`);
        }
        
        fs.writeFileSync(file, content);
        console.log(`Updated ${file}`);
    }
}
