import torch
from kornia.losses import ssim as dssim

def mse(image_pred, image_gt, valid_mask=None, reduction='mean'):
    value=(image_pred-image_gt)**2
    if valid_mask is not None:
        value = value[valid_mask]
    if reduction == 'mean':
        return torch.mean(value)
    return value

def mae(image_pred, image_gt):
    value=torch.abs(image_pred-image_gt)
    return  torch.mean(value)

#def psnr(image_pred, image_gt, valid_mask=None, reduction='mean'):
#    return -10*torch.log10(mse(image_pred, image_gt, valid_mask, reduction))

def psnr(image_pred, image_gt, valid_mask=None, reduction='mean'):
    value = 20*torch.log10(1/torch.sqrt(mse(image_pred, image_gt, valid_mask, reduction)))
    if reduction == 'mean':
        return torch.mean(value)
    return value

    
def ssim(image_pred, image_gt, reduction='mean'):
    """
    image_pred and image_gt: (3, H, W)
    """
    dssim_ = dssim(image_pred.unsqueeze(0), image_gt.unsqueeze(0), 3, reduction) # dissimilarity in [0, 1]
    return 1-2*dssim_ # in [-1, 1]