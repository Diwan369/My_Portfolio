# AWS S3 Setup Guide for Portfolio

## Problem Solved
Your resume and projects were disappearing because Render.com uses an ephemeral filesystem. Files stored locally are deleted when the dyno restarts. This solution uses AWS S3 for persistent storage.

## Setup Instructions

### Step 1: Create AWS Account & S3 Bucket

1. Go to [AWS Console](https://aws.amazon.com/)
2. Sign in or create a new account
3. Navigate to **S3 service**
4. Click **Create bucket** with these settings:
   - **Bucket name**: `portfolio-diwan-prod` (must be globally unique)
   - **Region**: `us-east-1` (or your preferred region)
   - **Block Public Access**: Keep all blocks enabled
   - Save the bucket name - you'll need it for environment variables

### Step 2: Create IAM User for S3 Access

1. Go to **IAM service** in AWS Console
2. Click **Users** → **Create user**
3. Name: `portfolio-s3-user`
4. Click **Next**
5. Choose **Attach policies directly**
6. Search for and attach: `AmazonS3FullAccess`
7. Click **Create user**
8. Click on the new user name
9. Go to **Security credentials** tab
10. Click **Create access key**
11. Choose **Application running outside AWS**
12. Click **Next** → **Create access key**
13. **Copy these values immediately**:
    - Access Key ID
    - Secret Access Key

### Step 3: Configure Render Environment Variables

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click your Portfolio service
3. Go to **Environment** tab
4. Add these environment variables:

```
AWS_STORAGE_BUCKET_NAME=portfolio-diwan-prod
AWS_ACCESS_KEY_ID=<paste your access key id>
AWS_SECRET_ACCESS_KEY=<paste your secret access key>
AWS_S3_REGION_NAME=us-east-1
```

5. Click **Save Changes**
6. Render will automatically redeploy your app

### Step 4: Verify It's Working

1. Wait 2-3 minutes for deployment to complete
2. Check Render dashboard for "Deploy succeeded"
3. Go to your portfolio website
4. Upload a resume or project image
5. Check AWS S3 console - you should see files in your bucket
6. Refresh the page multiple times - files should persist

## How It Works

- **Development (DEBUG=True)**: Files stored locally in `/media/`
- **Production (DEBUG=False)**: Files stored in AWS S3 bucket
- All static files and media uploads use S3 in production
- CDN integration with CloudFront is optional for faster delivery

## Important Notes

- AWS S3 has free tier: 5GB storage + 20,000 GET requests/month
- Keep your AWS keys secret - never commit them to GitHub
- If you exceed free tier, AWS charges ~$0.023/GB per month
- You can set up S3 lifecycle rules to delete old backups automatically

## Troubleshooting

### Files not uploading?
- Check that DEBUG is False on Render
- Verify AWS credentials are correct
- Check Render logs: `Deploy logs` tab

### High AWS costs?
- Check S3 bucket size in AWS Console
- Consider setting lifecycle policies to delete old backups
- Delete old uploads manually if needed

### Want to test locally?
- S3 works only when DEBUG=False
- To test S3 locally: Set DEBUG=False and add valid AWS credentials
- Alternative: Use `moto` package to mock S3 in tests

## Useful AWS CLI Commands (Optional)

List all files in bucket:
```bash
aws s3 ls s3://portfolio-diwan-prod/media/ --recursive
```

Delete all files (careful!):
```bash
aws s3 rm s3://portfolio-diwan-prod/media/ --recursive
```

## Additional Resources

- [Django Storages Documentation](https://django-storages.readthedocs.io/)
- [AWS S3 Pricing](https://aws.amazon.com/s3/pricing/)
- [Render Environment Variables](https://render.com/docs/environment-variables)
