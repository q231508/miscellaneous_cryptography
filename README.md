# Simple Crib Dragger

I am taking a cryptography course this semseter.
This week, while going through the slides, my professor was explaining OTP (One-Time pad).

From my understanding: OTP is a fairly effective form of encryption. If used correcty it is secure, but it is inefficient and sending the keys requires constant communication. If we use OTP for all messages, 
we might as well just send the plaintext message instead. This is because if we are comfortable sending messages and keys over a channel to the other party, we are probably already using a secure channel.

The general gist is that OTP works, but is too tedious to use it for every message due to key generation and delivery. 

With this in mind, my professor further explained that OTP can only be used once. We cannot reuse the same key to encrypt multiple messages.

To illustrate why, my professor provided us with two ciphertexts. 
She said that it was possible to find the plaintext messages if we first XOR the two ciphertexts. This is because XORing c1 and c2 will actually remove the key encryption from the XOR equation.

## $C_1 \oplus C_2 = (m_1 + k) \oplus (m_2 + k) = m_1 \oplus m_2 $ 

As we can see, we are then left with the XOR result of the two plaintexts. From here, it is possible to find the plaintexts by guessing words and XORing them with the result to try and reveal parts of $m_1$ or $m_2$. 
The process of revealing parts of the plaintexts is crib dragging. By using common words, names, and other phrases, we can slowly build parts of each plaintext by draggingthem across the XOR result of the two 
plaintexts and identifying any parts the look humanly legible. Once we manage to find the entirety of one of the plain texts, if we XOR it with the above result we will reveal the other one.

## $(m_1 \oplus m_2) \oplus m_2 = m_1$ 

SO the goal of crib dragging is to piece the plaintexts together by dragging a guess across $m_1 \oplus m_2$ letter by letter and doing:

$guess \oplus (m_1 \oplus m_2)$

at each position.

With this, we return to the two ciphertexts given in my class. It was only a passing comment, but my professor said we could try and decrypt the two cipher texts
to find the plaintext messages in our own time. As such, I have created a simple crib dragger that
can both automatically and manually check for words in the XOR result of the two ciphertexts. 

I have only ensured base functionality due to time constraints from other academic commitments. The algorithm has not been robustly reinforced nor extensively tested.

