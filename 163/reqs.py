def _is_newer_version(new, old):
    if new == '' or old == '':
        return False
    old_version_numbers = old.split('==')[1].split('.')
    new_version_numbers = new.split('==')[1].split('.')
    for old_level, new_level in zip(old_version_numbers, new_version_numbers):
        if int(old_level) < int(new_level):
            return True
        elif int(old_level) > int(new_level):
            return False
    return False


def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    changed = []
    for old, new in zip(old_reqs.splitlines(), new_reqs.splitlines()):
        if _is_newer_version(new, old):
            changed.append(old.split('==')[0])
    return changed
