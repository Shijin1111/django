# django
# next heading
`import java.io.File;
public class DirectoryLister
{
    public static void main(String args[])
    {
        String DirectoryPath = "C:/Users/shiji/Desktop/s2";
        String FileNametoSearch = "";
        listdirectories(DirectoryPath);
    }
    public static void listdirectories(String dir)
    {
        File directory = new File(dir);
        if(directory.exists() && directory.isDirectory())
        {
            listfilesanddirectories(directory);
        }
        else
        {
            System.out.print("directory not exist");
        }
    }`
