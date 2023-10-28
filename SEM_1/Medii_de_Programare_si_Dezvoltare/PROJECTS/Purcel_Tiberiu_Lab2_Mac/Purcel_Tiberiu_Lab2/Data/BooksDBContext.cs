using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using Purcel_Tiberiu_Lab2.Models;

namespace Purcel_Tiberiu_Lab2.Data
{
    public class BooksDBContext : DbContext
    {
        public BooksDBContext (DbContextOptions<BooksDBContext> options)
            : base(options)
        {
        }

        public DbSet<Purcel_Tiberiu_Lab2.Models.Book> Book { get; set; } = default!;

        public DbSet<Purcel_Tiberiu_Lab2.Models.Publisher> Publisher { get; set; } = default!;

        public DbSet<Purcel_Tiberiu_Lab2.Models.Author> Author { get; set; } = default!;
    }
}
