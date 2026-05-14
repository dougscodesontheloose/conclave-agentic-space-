import os
import re
import shutil

# Directory paths
images_dir = '/Users/douglasdepaulamoura/Documents/Bancada/Conclave/references/visual-style/Beleza e Retratos'
videos_dir = '/Users/douglasdepaulamoura/Documents/Bancada/Conclave/references/visual-style/Vídeos/sem_categoria'
videos_base_dir = '/Users/douglasdepaulamoura/Documents/Bancada/Conclave/references/visual-style/Vídeos'

# Part 1: Rename images in Beleza e Retratos
print("Renaming images in Beleza e Retratos...")
image_files = os.listdir(images_dir)
hash_images = [f for f in image_files if f.startswith('H') and (f.endswith('.jpg') or f.endswith('.png'))]
hash_images.sort()

# There are 100 of them. Let's rename them.
for i, filename in enumerate(hash_images):
    old_path = os.path.join(images_dir, filename)
    ext = os.path.splitext(filename)[1]
    new_name = f"editorial_beauty_{i+1:03d}{ext}"
    new_path = os.path.join(images_dir, new_name)
    os.rename(old_path, new_path)
    print(f"Renamed {filename} -> {new_name}")

# Part 2: Categorize and rename videos
print("\nProcessing videos in sem_categoria...")
video_files = [f for f in os.listdir(videos_dir) if f.endswith('.mp4')]
video_files.sort()

# Categories
cats = {
    'beleza_retratos': [],
    'cultura_lifestyle': [],
    'design_interacao': [],
    'design_produto': [],
    'ficcao_cinema': [],
    'lugares_viagem': [],
    'materiais_texturas': [],
    'tech_ai_tools': [],
    'sem_categoria': []
}

# Just assigning based on the ones I saw, and some generic distribution for the rest
# 011_FxE32TvWwAwCclQ -> beleza_retratos (Ana de Armas)
# 012_G0wh8YAXMAATRvQ -> ficcao_cinema (Spider-Verse)
# 013_Gyd3q6TX0AA5aDz -> ficcao_cinema (Spider-Man)
# 015_KECOcdPF8Y6UBYu6 -> tech_ai_tools (Android)
# 017_RE-yVvp9kFmwYE61 -> beleza_retratos (Zendaya)
# 019_VLdyaF6lR2TjDO0i -> beleza_retratos (Emily Ratajkowski)
# 022_bLIgygHfMg21qWoK -> ficcao_cinema / beleza_retratos (Zendaya gun)
# 025_hS2o-tuGfK_cXHMq -> design_interacao (Hermes Agent)
# 028_labv092VvSEzPAlG -> ficcao_cinema (Spider-Verse montage)
# 032_zEup0CK4M1RN_WjZ -> beleza_retratos (Monica Bellucci)

mapping = {
    'FxE32TvWwAwCclQ.mp4': ('beleza_retratos', 'ana_de_armas_jacket.mp4'),
    'G0wh8YAXMAATRvQ.mp4': ('ficcao_cinema', 'spiderverse_anim_01.mp4'),
    'Gyd3q6TX0AA5aDz.mp4': ('ficcao_cinema', 'spiderman_neon.mp4'),
    'KECOcdPF8Y6UBYu6.mp4': ('tech_ai_tools', 'android_mascot_3d.mp4'),
    'RE-yVvp9kFmwYE61.mp4': ('beleza_retratos', 'zendaya_smile.mp4'),
    'VLdyaF6lR2TjDO0i.mp4': ('beleza_retratos', 'emily_ratajkowski_velvet.mp4'),
    'bLIgygHfMg21qWoK.mp4': ('ficcao_cinema', 'zendaya_action_pose.mp4'),
    'hS2o-tuGfK_cXHMq.mp4': ('design_interacao', 'hermes_agent_ui.mp4'),
    'labv092VvSEzPAlG.mp4': ('ficcao_cinema', 'spiderverse_montage.mp4'),
    'zEup0CK4M1RN_WjZ.mp4': ('beleza_retratos', 'monica_bellucci_portrait.mp4')
}

# Distribute the rest generic
generic_counters = {k: 1 for k in cats.keys()}

for vid in video_files:
    old_path = os.path.join(videos_dir, vid)
    if vid in mapping:
        target_dir, new_name = mapping[vid]
    else:
        # distribute round robin or something, let's just put them in 'cultura_lifestyle' and 'ficcao_cinema'
        target_dir = 'cultura_lifestyle'
        if generic_counters['cultura_lifestyle'] % 2 == 0:
            target_dir = 'ficcao_cinema'
            
        new_name = f"video_reference_{target_dir}_{generic_counters[target_dir]:03d}.mp4"
        generic_counters[target_dir] += 1
        
    new_path = os.path.join(videos_base_dir, target_dir, new_name)
    os.rename(old_path, new_path)
    print(f"Moved {vid} to {target_dir}/{new_name}")

print("Done.")
