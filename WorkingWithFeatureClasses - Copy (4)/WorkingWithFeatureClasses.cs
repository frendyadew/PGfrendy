using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace WorkingWithFeatureClasses
{
    public class WorkingWithFeatureClasses : ESRI.ArcGIS.Desktop.AddIns.Button
    {
        frmFeatureClasses formFeatureClasses;
        public WorkingWithFeatureClasses()
        {
        }

        protected override void OnClick()
        {
            if (formFeatureClasses == null || formFeatureClasses.IsDisposed)
                formFeatureClasses = new frmFeatureClasses();

                if (!formFeatureClasses.Visible)
                    formFeatureClasses.Show(null);

            ArcMap.Application.CurrentTool = null;
        }
        protected override void OnUpdate()
        {
            Enabled = ArcMap.Application != null;
        }
    }

}
