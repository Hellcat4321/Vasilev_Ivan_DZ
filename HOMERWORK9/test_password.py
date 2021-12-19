import password

class Test_password_word():
        def test_true_password_1_duwud75(self):
            assert password.password("duwud75") == True
        
        def test_length_password_duw(self):
            assert password.password("duw") == False

        def test_not_only_numders_in_password_543543(self):
            assert password.password("543543") == False

        def test_not_numders_in_password_erwrewer(self):
            assert password.password("erwrewer") == False

        def test_password_in_password_1_password1(self):
            assert password.password("password1") == False
        
        def test_password_in_password_2_PaSswOrd1(self):
            assert password.password("PaSswOrd1") == False

        def test_password_in_password_3_PASSWORD1(self):
            assert password.password("PASSWORD1") == False
        
        def test_true_password_2_PaSs1wOrd(self):
            assert password.password("PaSs1wOrd") == True
        
        def test_true_password_2_dWTFtFd345f(self):
            assert password.password("dWTFtFd345f") == True