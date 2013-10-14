# (c) 2012, Michael DeHaan <michael.dehaan@gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

from ansible.utils import safe_eval
import ansible.utils as utils
import ansible.errors as errors

def flatten(terms):
    ret = []
    for term in terms:
        if isinstance(term, list):
            ret.extend(term)
        else:
            ret.append(term)
    return ret

class LookupModule(object):

    def __init__(self, basedir=None, **kwargs):
        self.basedir = basedir

    def run(self, terms, inject=None, **kwargs):
        terms = utils.listify_lookup_plugin_terms(terms, self.basedir, inject) 

        if isinstance(terms, dict):
            # This way if want tuples: item[0] or item[1].name
            #terms = [i for i in terms.iteritems]
            # This way if want hash: item.key or item.value.name
            terms = [{"key":i[0], "value":i[1]} for i in terms.iteritems]
        if not isinstance(terms, list):
            raise errors.AnsibleError("with_items expects a list or a hash")

        return flatten(terms)


