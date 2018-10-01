# Active Record Queries

In this challenge you'll be working with a single model, `Product`. The database schema has already been created for you.


## Release 0: Setup

Start the challenge by creating the test database and running migrations to create your tables & columns:

```bash
$ rake db:drop APP_ENV=test
$ rake db:create APP_ENV=test
$ rake db:migrate APP_ENV=test
$ rake db:seed APP_ENV=test
```

Fortunately, multiple rake tasks can be combined into a single command:

```bash
$ rake db:drop db:create db:migrate db:seed APP_ENV=test
```

> We specify `APP_ENV=test` because we're going to be working with the **test** database, not in the development console. If you want to create a database in the development environment, you can drop the `APP_ENV=test` - it defaults to development. Specifically, that would look like:

```bash
$ rake db:drop db:create db:migrate db:seed
```

## Release 1: Pass the Tests

Once you've setup the app, your goal is to get all the below tests passing:

```
bundle exec rspec spec/product_crud_spec.rb
```

Prepending with `bundle exec` will force RSPEC to run with the versions of gems found in `Gemfile.lock` rather than your system's version of RSPEC. This allows for developers with multiple versions of gems to all work at the same pace as each other.

The `ProductCrud` class has a number of methods for you to implement. As you work, follow the spec file & review the method names carefully. Every method can be implemented with ActiveRecord alone.

A `Product` record in the database looks like this:

```ruby
#<Product id: 30, manufacturer: "Wiza-Ritchie", model: "Rustic Silk Computer", category: "Industrial", description: "Bespoke helvetica godard pork belly keytar skatebo...", price_cents: 3499, rating: 1.6, volume_discount_percent: 6, volume_discount_threshold: 10, color: "maroon", created_at: "2017-10-04 21:29:48", updated_at: "2017-10-04 21:29:48">
```

Need A Hint? Check out the available [methods for ActiveRecord](http://guides.rubyonrails.org/active_record_querying.html).
