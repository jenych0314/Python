from numpy import*
import matplotlib.pyplot as plt
from random import*
import math

def rot_range(block_idx):

    rot = 0

    if block_idx == 1:
        rot = 1
    elif block_idx == 2 or block_idx == 4 or block_idx == 5:
        rot = 2
    elif block_idx == 3 or block_idx == 6 or block_idx == 7:
        rot = 4
    
    return rot


#get line erase
def block_erase(board):

    score = 0

    for i_idx in reversed(range(2,20)):
        line = board[i_idx,:]
        line_TF = line > 0

        if line_TF.sum() == 10:
            board[1:i_idx + 1,:] = board[0:i_idx,:]
            score += 1
    
    return score, board


def get_rand_rot(block_idx):

    if block_idx == 1:
        rot = 1

    elif block_idx == 2 or block_idx == 4 or block_idx == 5:
        rot = randrange(1,3)
    
    elif block_idx == 3 or block_idx == 6 or block_idx == 7:
        rot = randrange(1,5)
    
    return rot


def visualize(board_final, idx, save):

    filename = 'result/' + '%.5d' % idx + '.png'

    image = zeros([20,10,3])

    for i_idx in range(20):
        for j_idx in range(10):
            cr, cg, cb = get_color(board_final[i_idx,j_idx])

            image[i_idx,j_idx,0] = cr
            image[i_idx,j_idx,1] = cg
            image[i_idx,j_idx,2] = cb

    plt.imshow(image/255)
    if save:
        plt.savefig(filename)
    plt.show()


def get_block(block_idx, rot):

    blocks = []

    #1
    #■■
    #■■
    if block_idx == 1:
        blocks = ones([2,2])
    
    #2
    if block_idx == 2 and rot == 1:
        blocks = ones([4,1])
    #■■■■
    elif block_idx == 2 and rot == 2:
        blocks = ones([4,1])
    #■
    #■
    #■
    #■

    #3
    if block_idx == 3 and rot == 1:
    #□□□
    #■■■
    #□■□
        blocks = zeros([3,3])
        blocks[1,0] = 1
        blocks[1,1] = 1
        blocks[1,2] = 1
        blocks[2,1] = 1
    
    elif block_idx == 3 and rot == 2:
    #□■□
    #■■□
    #□■□
        blocks = zeros([3,3])
        blocks[0,1] = 1
        blocks[1,0] = 1
        blocks[1,1] = 1
        blocks[2,1] = 1
    
    elif block_idx == 3 and rot == 3:
    #□□□
    #□■□
    #■■■
        blocks = zeros([3,3])
        blocks[2,0] = 1
        blocks[2,1] = 1
        blocks[1,1] = 1
        blocks[2,2] = 1
    
    elif block_idx == 3 and rot == 4:
    #■□□
    #■■□
    #■□□
        blocks = zeros([3,3])
        blocks[0,0] = 1
        blocks[1,0] = 1
        blocks[1,1] = 1
        blocks[2,0] = 1
    
    #4
    if block_idx == 4 and rot == 1:
    #□□□
    #■■□
    #□■■
        blocks = zeros([3,3])
        blocks[1,0] = 1
        blocks[1,1] = 1
        blocks[2,1] = 1
        blocks[2,2] = 1
    
    elif block_idx == 4 and rot == 2:
    #□■□
    #■■□
    #■□□
        blocks = zeros([3,3])
        blocks[0,1] = 1
        blocks[1,0] = 1
        blocks[1,1] = 1
        blocks[2,0] = 1
    
    #5
    if block_idx == 5 and rot == 1:
    #□□□
    #□■■
    #■■□
        blocks = zeros([3,3])
        blocks[1,1] = 1
        blocks[1,2] = 1
        blocks[2,0] = 1
        blocks[2,1] = 1
    
    elif block_idx == 5 and rot == 2:
    #■□□
    #■■□
    #□■□
        blocks = zeros([3,3])
        blocks[0,0] = 1
        blocks[1,0] = 1
        blocks[1,1] = 1
        blocks[2,1] = 1
    
    #6
    if block_idx == 6 and rot == 1:
    #□□□
    #■■■
    #■□□
        blocks = zeros([3,3])
        blocks[1,0] = 1
        blocks[1,1] = 1
        blocks[1,2] = 1
        blocks[2,0] = 1
    
    elif block_idx == 6 and rot == 2:
    #■□□
    #■□□
    #■■□
        blocks = zeros([3,3])
        blocks[0,0] = 1
        blocks[1,0] = 1
        blocks[2,0] = 1
        blocks[2,1] = 1
    
    elif block_idx == 6 and rot == 3:
    #□□□
    #□□■
    #■■■
        blocks = zeros([3,3])
        blocks[1,2] = 1
        blocks[2,0] = 1
        blocks[2,1] = 1
        blocks[2,2] = 1
    
    elif block_idx == 6 and rot == 4:
    #■■□
    #□■□
    #□■□
        blocks = zeros([3,3])
        blocks[0,0] = 1
        blocks[0,1] = 1
        blocks[1,1] = 1
        blocks[2,1] = 1

    #7
    if block_idx == 7 and rot == 1:
    #□□□
    #■■■
    #□□■
        blocks = zeros([3,3])
        blocks[1,0] = 1
        blocks[1,1] = 1
        blocks[1,2] = 1
        blocks[2,2] = 1
    
    elif block_idx == 7 and rot == 2:
    #■■□
    #■□□
    #■□□
        blocks = zeros([3,3])
        blocks[0,0] = 1
        blocks[0,1] = 1
        blocks[1,0] = 1
        blocks[2,0] = 1
    
    elif block_idx == 7 and rot == 3:
    #□□□
    #■□□
    #■■■
        blocks = zeros([3,3])
        blocks[1,0] = 1
        blocks[2,0] = 1
        blocks[2,1] = 1
        blocks[2,2] = 1
    
    elif block_idx == 7 and rot == 4:
    #□■□
    #□■□
    #■■□
        blocks = zeros([3,3])
        blocks[0,1] = 1
        blocks[1,1] = 1
        blocks[2,0] = 1
        blocks[2,1] = 1

    return blocks


def get_max_pos(block_idx, rot, blocks):
    max_pos = 0

    if block_idx == 1:
        max_pos = 8

    elif block_idx == 2:

        if rot == 1:
            max_pos = 6

        elif rot == 2:
            max_pos = 9
    
    elif block_idx >= 3:

        last_col = blocks[:,2].sum()

        if last_col == 0:
            max_pos = 8

        else:
            max_pos = 7

    return max_pos


def get_color(block_idx):
    cr = 0
    cg = 0
    cb = 0

    if block_idx == 0:
        cr = 0
        cg = 0
        cb = 0
    
    #1
    elif block_idx == 1:
        cr = 100
        cg = 100
        cb = 255
    
    #2
    elif block_idx == 2:
        cr = 255
        cg = 100
        cb = 100

    #3
    elif block_idx == 3:
        cr = 128
        cg = 255
        cb = 128

    #4
    elif block_idx == 4:
        cr = 128
        cg = 128
        cb = 255

    #5
    elif block_idx == 5:
        cr = 255
        cg = 255
        cb = 128

    #6
    elif block_idx == 6:
        cr = 192
        cg = 192
        cb = 192

    #7
    elif block_idx == 7:
        cr = 128
        cg = 255
        cb = 255

    return cr, cg, cb


def board2vec(board_final):

    matrix = board_final > 0
    matrix = matrix * 1

    vec = zeros(10)

    for i_idx in range(10):
        for j_idx in range(20):

            if matrix[j_idx,i_idx] != 0:
                vec[i_idx] = j_idx/20
                break
    
    return vec


def output2pos_rot(block_idx, output):

    out1 = output[0] #rotation
    out2 = output[1] #position

    if block_idx == 1:
        rot = 1
    
    elif block_idx == 2 or block_idx == 4 or block_idx == 5:
        rot = math.floor(output[0] * 2 - 0.00000001) + 1 #1,2
    
    elif block_idx == 3 or block_idx == 6 or block_idx == 7:
        rot = math.floor(output[0] * 4 - 0.00000001) + 1 #1,2,3,4

    pos = math.floor(output[0] * 10 - 0.00000001)

    return rot, pos


def get_value(roi):

    val = 0
    if (roi[2,:] > 0).sum() == 3:
        val = 3
        if (roi[1,:] > 0).sum() == 3:
            val = 6
            if (roi[0,:] > 0).sum() == 3:
                val = 9
    
    else:
        val = (roi[2,:] > 0).sum()

    return val


def get_value_4(roi):

    val = 0
    if (roi[3,:] > 0).sum() == 3: # down if perfect
        val = 0
        if(roi[2,:] > 0).sum() == 3:
            val = 6
            if(roi[0,:] > 0).sum() == 3:
                val = 9
    else:
        val = (roi[3,:] > 0).sum()

    return val


def is_hole(vec): #when put the block if it makes hole then going to panalty

    val = 0
    vec = vec > 0
    vec = vec * 1

    for i_idx in range(len(roi[:,0]) - 1):
        if vec[i_idx] == 1 and vec[i_idx] == 0:
            val = -6
    
    return val


# block_idx = randrange(1, num_of_blocks + 1)
# rot_range = rot_range(block_idx)

# max_i = 0
# max_y = 0

# for i_idx in range(rot_range):

#     rot = i_idx + 1
#     blocks = get_block(block_idx, rot) * block_idx
#     max_pos = get_max_pos(block_idx, rot, blocks)

#     for j_idx in range(max_pos + 1):
#         position = j_idx
#         bH, bW = blocks.shape
#         board_temp = copy(board)
#         board_temp[:,10] = 1

#         max_step = 0

#         for step in range(21 - bH):

#             roi = board_temp[step:step + bH, position:position + bW]
#             col_mul = multiply(roi, blocks)

#             if col_mul.sum() == 0:
#                 max_step = step
#             else:
#                 break
        
#         board_temp[]