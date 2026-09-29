content = open('index.html', 'r', encoding='utf-8').read()
replacements = {
    '<div class=\"spotlight-card card-beige\">': '<div class=\"spotlight-card card-beige\" onclick=\"window.location.href=\'full-home-cleaning.html\'\" style=\"cursor: pointer;\">',
    '<div class=\"spotlight-card card-grey\">': '<div class=\"spotlight-card card-grey\" onclick=\"window.location.href=\'ac-service.html\'\" style=\"cursor: pointer;\">',
    '<div class=\"spotlight-card card-blue\">': '<div class=\"spotlight-card card-blue\" onclick=\"window.location.href=\'electrician.html\'\" style=\"cursor: pointer;\">',
    '<div class=\"spotlight-card card-pest\">': '<div class=\"spotlight-card card-pest\" onclick=\"window.location.href=\'pest-control.html\'\" style=\"cursor: pointer;\">',
    '<div class=\"spotlight-card card-olive\">': '<div class=\"spotlight-card card-olive\" onclick=\"window.location.href=\'spa-women.html\'\" style=\"cursor: pointer;\">',
}
for old, new in replacements.items(): content = content.replace(old, new)

noteworthy_links = ['full-home-cleaning.html', 'painting.html', 'living-bedroom.html', 'water-purifier.html', 'kitchen-cleaning.html', 'hair-studio.html', 'ac-service.html']
parts = content.split('<div class=\"noteworthy-item\">')
if len(parts) - 1 == len(noteworthy_links):
    new_content = parts[0]
    for i, link in enumerate(noteworthy_links):
        new_content += f'<div class=\"noteworthy-item\" onclick=\"window.location.href=\'{link}\'\" style=\"cursor: pointer;\">' + parts[i+1]
    open('index.html', 'w', encoding='utf-8').write(new_content)
    print('Success')
else:
    print('Mismatch')
