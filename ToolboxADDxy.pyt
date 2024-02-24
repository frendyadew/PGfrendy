import arcpy

def add_xy_coordinates(input_layer, output_layer):
    # Periksa apakah layer memiliki data spasial
    if not arcpy.Describe(input_layer).spatialReference:
        arcpy.AddMessage("Layer tidak memiliki informasi koordinat spasial.")
        return

    # Salin layer ke layer baru dengan nama yang berbeda
    arcpy.CopyFeatures_management(input_layer, output_layer)

    # Tambahkan kolom X dan Y jika belum ada
    if "X" not in [field.name for field in arcpy.ListFields(output_layer)]:
        arcpy.AddField_management(output_layer, "X", "DOUBLE")
    if "Y" not in [field.name for field in arcpy.ListFields(output_layer)]:
        arcpy.AddField_management(output_layer, "Y", "DOUBLE")

    # Hitung dan tambahkan koordinat X&Y
    with arcpy.da.UpdateCursor(output_layer, ["SHAPE@", "X", "Y"]) as cursor:
        for row in cursor:
            row[1] = row[0].centroid.X
            row[2] = row[0].centroid.Y
            cursor.updateRow(row)

    arcpy.RefreshActiveView()
    arcpy.AddMessage("Koordinat X&Y telah ditambahkan ke layer baru.")

# Panggil fungsi ketika skrip dijalankan
if __name__ == "__main__":
    # Ambil layer sebagai parameter input
    input_layer = arcpy.GetParameterAsText(0)

    # Tentukan nama layer baru sebagai parameter output
    output_layer = arcpy.GetParameterAsText(1)

    add_xy_coordinates(input_layer, output_layer)
