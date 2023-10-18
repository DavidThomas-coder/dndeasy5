const getDatabaseUrl = (nodeEnv) => {
  return (
    {
      development: "postgres://postgres:postgres@localhost:5432/dndeasy_development",
      test: "postgres://postgres:postgres@localhost:5432/dndeasy_test",
      e2e: "postgres://postgres:postgres@localhost:5432/dndeasy_e2e",
    }[nodeEnv] || process.env.DATABASE_URL
  );
};

module.exports = getDatabaseUrl;
