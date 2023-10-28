using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Purcel_Tiberiu_Lab2.Migrations
{
    /// <inheritdoc />
    public partial class AuthorUpdate : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "FullName",
                table: "Author");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "FullName",
                table: "Author",
                type: "TEXT",
                nullable: false,
                defaultValue: "");
        }
    }
}
