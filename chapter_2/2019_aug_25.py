# 2-3: personal message
name = 'susan';
print(f"{name}");

# 2-4: name cases
name = 'james';
print(f"{name.lower()}");
print(f"{name.upper()}");
print(f"{name.title()}");


# 2-5: famous quote
quote = "'If you don't design your own life plan, chances are you'll fall into someone else's plan. And guess what they have planned for you? Not much.'";
print(f"Jim Rohn once said, {quote}");

# 2-6: famous quote 2

famous_person = 'Jim Rohn';
message = f"{famous_person} once said, {quote}"
print(message)

# 2-6: stripping names
name = '\tSarah\n';
print(name);
print(name.lstrip());
print(name.rstrip());
print(name.strip());
