using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using Purcel_Tiberiu_Lab2.Data;
using Purcel_Tiberiu_Lab2.Models;

namespace Purcel_Tiberiu_Lab2.Pages.Books
{
    public class IndexModel : PageModel
    {
        private readonly Purcel_Tiberiu_Lab2.Data.BooksDBContext _context;

        public IndexModel(Purcel_Tiberiu_Lab2.Data.BooksDBContext context)
        {
            _context = context;
        }

        public IList<Book> Book { get;set; } = default!;

        public async Task OnGetAsync()
        {
            if (_context.Book != null)
            {
                Book = await _context.Book.Include(b=>b.Publisher).Include(c=>c.Author).ToListAsync();
            }
        }
    }
}
