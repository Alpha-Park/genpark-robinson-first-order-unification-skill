class FirstOrderUnifier:
    """
    Robinson's First-Order Term Unification Algorithm.
    Computes most general unifier (MGU) substitution for symbolic terms.
    """
    def unify(self, term1, term2):
        subst = {}
        if self._unify_terms(term1, term2, subst):
            return subst
        return None

    def _unify_terms(self, t1, t2, s):
        t1 = self._apply(t1, s)
        t2 = self._apply(t2, s)

        if t1 == t2:
            return True

        if self._is_var(t1):
            if self._occurs(t1, t2):
                return False
            s[t1] = t2
            return True

        if self._is_var(t2):
            if self._occurs(t2, t1):
                return False
            s[t2] = t1
            return True

        if isinstance(t1, tuple) and isinstance(t2, tuple):
            if t1[0] != t2[0] or len(t1) != len(t2):
                return False
            for arg1, arg2 in zip(t1[1:], t2[1:]):
                if not self._unify_terms(arg1, arg2, s):
                    return False
            return True

        return False

    def _is_var(self, t):
        return isinstance(t, str) and t.startswith("?")

    def _occurs(self, var, term):
        if var == term:
            return True
        if isinstance(term, tuple):
            return any(self._occurs(var, arg) for arg in term[1:])
        return False

    def _apply(self, term, s):
        if self._is_var(term):
            return s.get(term, term)
        if isinstance(term, tuple):
            return (term[0],) + tuple(self._apply(arg, s) for arg in term[1:])
        return term
