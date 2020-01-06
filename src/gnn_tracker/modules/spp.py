import torch
from torch import nn

import math


class SpatialPyramidPool(nn.Module):

    def forward(self, inp, levels):
        """
        Args:
            inp: Output tensor from a CNN of shape [b, c, h, w].
            levels: List of integers with number of grid cells for every pooling level.

        Returns:
             A tensor vector with shape [1 x n] with concentration of the multi-level pooling.
        """
        b, c, h, w = inp.shape
        out = []
        for i in range(len(levels)):
            h_wid = int(math.ceil(h / levels[i]))
            w_wid = int(math.ceil(w / levels[i]))
            h_pad = (h_wid * levels[i] - h + 1) / 2
            w_pad = (w_wid * levels[i] - w + 1) / 2
            maxpool = nn.MaxPool2d((h_wid, w_wid), stride=(h_wid, w_wid), padding=(h_pad, w_pad))
            out.append(maxpool(inp))

        return torch.cat(out, dim=1)
