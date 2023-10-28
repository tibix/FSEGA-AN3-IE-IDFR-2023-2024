using System;
namespace Purcel_Tiberiu_Lab2.Models
{
	public class Author
	{
		public int ID { get; set; }
		public string FirstName { get; set; }
		public string LastName { get; set; }

        public string? FullName
        {
            get
            {
                return string.IsNullOrWhiteSpace(FirstName) && string.IsNullOrWhiteSpace(LastName)
                ? null
                : $"{FirstName} {LastName}".Trim();
            }
        }

        public ICollection<Book>? Books { get; set; }

    }
}