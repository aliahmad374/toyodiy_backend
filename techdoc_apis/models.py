from django.db import models

# Create your models here.


class Eztb3105(models.Model):
    id = models.BigIntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    itemid = models.TextField(db_column='ItemID', blank=True, null=True)  # Field name made lowercase.
    itemname = models.TextField(db_column='ItemName', blank=True, null=True)  # Field name made lowercase.
    mastercard = models.TextField(db_column='MasterCard', blank=True, null=True)  # Field name made lowercase.
    ref1 = models.TextField(db_column='Ref1', blank=True, null=True)  # Field name made lowercase.
    ref2 = models.TextField(db_column='Ref2', blank=True, null=True)  # Field name made lowercase.
    ref3 = models.TextField(db_column='Ref3', blank=True, null=True)  # Field name made lowercase.
    ref4 = models.TextField(db_column='Ref4', blank=True, null=True)  # Field name made lowercase.
    ref5 = models.TextField(db_column='Ref5', blank=True, null=True)  # Field name made lowercase.
    group1 = models.TextField(db_column='Group1', blank=True, null=True)  # Field name made lowercase.
    group2 = models.TextField(db_column='Group2', blank=True, null=True)  # Field name made lowercase.
    group3 = models.TextField(db_column='Group3', blank=True, null=True)  # Field name made lowercase.
    group4 = models.TextField(db_column='Group4', blank=True, null=True)  # Field name made lowercase.
    group5 = models.TextField(db_column='Group5', blank=True, null=True)  # Field name made lowercase.
    group6 = models.TextField(db_column='Group6', blank=True, null=True)  # Field name made lowercase.
    group7 = models.TextField(db_column='Group7', blank=True, null=True)  # Field name made lowercase.
    multigrp1 = models.TextField(db_column='MultiGrp1', blank=True, null=True)  # Field name made lowercase.
    multigrp2 = models.TextField(db_column='MultiGrp2', blank=True, null=True)  # Field name made lowercase.
    multigrp3 = models.TextField(db_column='MultiGrp3', blank=True, null=True)  # Field name made lowercase.
    multigrp4 = models.TextField(db_column='MultiGrp4', blank=True, null=True)  # Field name made lowercase.
    multigrp5 = models.TextField(db_column='MultiGrp5', blank=True, null=True)  # Field name made lowercase.
    color = models.TextField(db_column='Color', blank=True, null=True)  # Field name made lowercase.
    cat = models.TextField(db_column='Cat', blank=True, null=True)  # Field name made lowercase.
    catcode = models.TextField(db_column='CatCode', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    desc1 = models.TextField(db_column='Desc1', blank=True, null=True)  # Field name made lowercase.
    desc2 = models.TextField(db_column='Desc2', blank=True, null=True)  # Field name made lowercase.
    movement = models.TextField(db_column='Movement', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    origcountry = models.TextField(db_column='OrigCountry', blank=True, null=True)  # Field name made lowercase.
    fob = models.DecimalField(db_column='FOB', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    costprice = models.DecimalField(db_column='CostPrice', max_digits=21, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    currprice = models.DecimalField(db_column='CurrPrice', max_digits=21, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    costcode = models.TextField(db_column='CostCode', blank=True, null=True)  # Field name made lowercase.
    importcurr = models.TextField(db_column='ImportCurr', blank=True, null=True)  # Field name made lowercase.
    usamt = models.DecimalField(db_column='USAmt', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    usexch = models.DecimalField(db_column='USExch', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    importexch = models.DecimalField(db_column='ImportExch', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    price1 = models.DecimalField(db_column='Price1', max_digits=21, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    price2 = models.DecimalField(db_column='Price2', max_digits=21, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    price3 = models.DecimalField(db_column='Price3', max_digits=21, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    price4 = models.DecimalField(db_column='Price4', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    price5 = models.DecimalField(db_column='Price5', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    price6 = models.DecimalField(db_column='Price6', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    price7 = models.DecimalField(db_column='Price7', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    price8 = models.DecimalField(db_column='Price8', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    price9 = models.DecimalField(db_column='Price9', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    fixedprice = models.DecimalField(db_column='FixedPrice', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    netprice = models.DecimalField(db_column='NetPrice', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    fixperc = models.DecimalField(db_column='FixPerc', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    barcodeunit = models.TextField(db_column='BarCodeUnit', blank=True, null=True)  # Field name made lowercase.
    barcodepack = models.TextField(db_column='BarCodePack', blank=True, null=True)  # Field name made lowercase.
    uom = models.TextField(db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    quaperunit = models.DecimalField(db_column='QuaPerUnit', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    packunit = models.TextField(db_column='PackUnit', blank=True, null=True)  # Field name made lowercase.
    quaperpack = models.DecimalField(db_column='QuaPerPack', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    flength = models.DecimalField(db_column='fLength', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    fwidth = models.DecimalField(db_column='fWidth', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    fheight = models.DecimalField(db_column='fHeight', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    fvolume = models.DecimalField(db_column='fVolume', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    fweight = models.DecimalField(db_column='fWeight', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc01 = models.DecimalField(db_column='Loc01', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc02 = models.DecimalField(db_column='Loc02', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc03 = models.DecimalField(db_column='Loc03', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc04 = models.DecimalField(db_column='Loc04', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc05 = models.DecimalField(db_column='Loc05', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc06 = models.DecimalField(db_column='Loc06', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc07 = models.DecimalField(db_column='Loc07', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc08 = models.DecimalField(db_column='Loc08', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc09 = models.DecimalField(db_column='Loc09', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc10 = models.DecimalField(db_column='Loc10', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc11 = models.DecimalField(db_column='Loc11', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc12 = models.DecimalField(db_column='Loc12', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc13 = models.DecimalField(db_column='Loc13', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc14 = models.DecimalField(db_column='Loc14', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc15 = models.DecimalField(db_column='Loc15', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc16 = models.DecimalField(db_column='Loc16', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc17 = models.DecimalField(db_column='Loc17', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc18 = models.DecimalField(db_column='Loc18', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc19 = models.DecimalField(db_column='Loc19', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc20 = models.DecimalField(db_column='Loc20', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    reorder = models.BigIntegerField(db_column='ReOrder', blank=True, null=True)  # Field name made lowercase.
    reord01 = models.BigIntegerField(db_column='ReOrd01', blank=True, null=True)  # Field name made lowercase.
    reord02 = models.BigIntegerField(db_column='ReOrd02', blank=True, null=True)  # Field name made lowercase.
    reord03 = models.BigIntegerField(db_column='ReOrd03', blank=True, null=True)  # Field name made lowercase.
    reord04 = models.BigIntegerField(db_column='ReOrd04', blank=True, null=True)  # Field name made lowercase.
    reord05 = models.BigIntegerField(db_column='ReOrd05', blank=True, null=True)  # Field name made lowercase.
    reord06 = models.BigIntegerField(db_column='ReOrd06', blank=True, null=True)  # Field name made lowercase.
    reord07 = models.BigIntegerField(db_column='ReOrd07', blank=True, null=True)  # Field name made lowercase.
    reord08 = models.BigIntegerField(db_column='ReOrd08', blank=True, null=True)  # Field name made lowercase.
    reord09 = models.BigIntegerField(db_column='ReOrd09', blank=True, null=True)  # Field name made lowercase.
    reord10 = models.BigIntegerField(db_column='ReOrd10', blank=True, null=True)  # Field name made lowercase.
    reord11 = models.BigIntegerField(db_column='ReOrd11', blank=True, null=True)  # Field name made lowercase.
    reord12 = models.BigIntegerField(db_column='ReOrd12', blank=True, null=True)  # Field name made lowercase.
    reord13 = models.BigIntegerField(db_column='ReOrd13', blank=True, null=True)  # Field name made lowercase.
    reord14 = models.BigIntegerField(db_column='ReOrd14', blank=True, null=True)  # Field name made lowercase.
    reord15 = models.BigIntegerField(db_column='ReOrd15', blank=True, null=True)  # Field name made lowercase.
    reord16 = models.BigIntegerField(db_column='ReOrd16', blank=True, null=True)  # Field name made lowercase.
    reord17 = models.BigIntegerField(db_column='ReOrd17', blank=True, null=True)  # Field name made lowercase.
    reord18 = models.BigIntegerField(db_column='ReOrd18', blank=True, null=True)  # Field name made lowercase.
    reord19 = models.BigIntegerField(db_column='ReOrd19', blank=True, null=True)  # Field name made lowercase.
    reord20 = models.BigIntegerField(db_column='ReOrd20', blank=True, null=True)  # Field name made lowercase.
    binloc01 = models.TextField(db_column='BinLoc01', blank=True, null=True)  # Field name made lowercase.
    binloc02 = models.TextField(db_column='BinLoc02', blank=True, null=True)  # Field name made lowercase.
    binloc03 = models.TextField(db_column='BinLoc03', blank=True, null=True)  # Field name made lowercase.
    binloc04 = models.TextField(db_column='BinLoc04', blank=True, null=True)  # Field name made lowercase.
    binloc05 = models.TextField(db_column='BinLoc05', blank=True, null=True)  # Field name made lowercase.
    binloc06 = models.TextField(db_column='BinLoc06', blank=True, null=True)  # Field name made lowercase.
    binloc07 = models.TextField(db_column='BinLoc07', blank=True, null=True)  # Field name made lowercase.
    binloc08 = models.TextField(db_column='BinLoc08', blank=True, null=True)  # Field name made lowercase.
    binloc09 = models.TextField(db_column='BinLoc09', blank=True, null=True)  # Field name made lowercase.
    binloc10 = models.TextField(db_column='BinLoc10', blank=True, null=True)  # Field name made lowercase.
    autopic01 = models.TextField(db_column='AutoPic01', blank=True, null=True)  # Field name made lowercase.
    autopic02 = models.TextField(db_column='AutoPic02', blank=True, null=True)  # Field name made lowercase.
    autopic03 = models.TextField(db_column='AutoPic03', blank=True, null=True)  # Field name made lowercase.
    autopic04 = models.TextField(db_column='AutoPic04', blank=True, null=True)  # Field name made lowercase.
    autopic05 = models.TextField(db_column='AutoPic05', blank=True, null=True)  # Field name made lowercase.
    autopic06 = models.TextField(db_column='AutoPic06', blank=True, null=True)  # Field name made lowercase.
    autopic07 = models.TextField(db_column='AutoPic07', blank=True, null=True)  # Field name made lowercase.
    autopic08 = models.TextField(db_column='AutoPic08', blank=True, null=True)  # Field name made lowercase.
    autopic09 = models.TextField(db_column='AutoPic09', blank=True, null=True)  # Field name made lowercase.
    autopic10 = models.TextField(db_column='AutoPic10', blank=True, null=True)  # Field name made lowercase.
    cogsacccode = models.TextField(db_column='COGSAccCode', blank=True, null=True)  # Field name made lowercase.
    cogsaccname = models.TextField(db_column='COGSAccName', blank=True, null=True)  # Field name made lowercase.
    incacccode = models.TextField(db_column='IncAccCode', blank=True, null=True)  # Field name made lowercase.
    incaccname = models.TextField(db_column='IncAccName', blank=True, null=True)  # Field name made lowercase.
    assetacccode = models.TextField(db_column='AssetAccCode', blank=True, null=True)  # Field name made lowercase.
    assetaccname = models.TextField(db_column='AssetAccName', blank=True, null=True)  # Field name made lowercase.
    qb2008itemcode = models.TextField(db_column='QB2008ItemCode', blank=True, null=True)  # Field name made lowercase.
    qb2008itemname = models.TextField(db_column='QB2008ItemName', blank=True, null=True)  # Field name made lowercase.
    qb2008taxrefcode = models.TextField(db_column='QB2008TaxRefCode', blank=True, null=True)  # Field name made lowercase.
    mark1 = models.IntegerField(db_column='Mark1', blank=True, null=True)  # Field name made lowercase.
    mark2 = models.IntegerField(db_column='Mark2', blank=True, null=True)  # Field name made lowercase.
    mark3 = models.IntegerField(db_column='Mark3', blank=True, null=True)  # Field name made lowercase.
    mark4 = models.IntegerField(db_column='Mark4', blank=True, null=True)  # Field name made lowercase.
    mark5 = models.IntegerField(db_column='Mark5', blank=True, null=True)  # Field name made lowercase.
    mark6 = models.IntegerField(db_column='Mark6', blank=True, null=True)  # Field name made lowercase.
    mark7 = models.IntegerField(db_column='Mark7', blank=True, null=True)  # Field name made lowercase.
    mark8 = models.IntegerField(db_column='Mark8', blank=True, null=True)  # Field name made lowercase.
    itemtype = models.TextField(db_column='ItemType', blank=True, null=True)  # Field name made lowercase.
    taxstatus = models.TextField(db_column='TaxStatus', blank=True, null=True)  # Field name made lowercase.
    locdam = models.BigIntegerField(db_column='LocDam', blank=True, null=True)  # Field name made lowercase.
    locres = models.BigIntegerField(db_column='LocRes', blank=True, null=True)  # Field name made lowercase.
    locsam = models.BigIntegerField(db_column='LocSam', blank=True, null=True)  # Field name made lowercase.
    vatcode = models.CharField(db_column='VATCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    vatdesc = models.TextField(db_column='VATDesc', blank=True, null=True)  # Field name made lowercase.
    vatval = models.DecimalField(db_column='VATVal', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    defprice = models.BigIntegerField(db_column='DefPrice', blank=True, null=True)  # Field name made lowercase.
    whlimit = models.DecimalField(db_column='WhLimit', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    avrcost = models.DecimalField(db_column='AvrCost', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    todaycost = models.DecimalField(db_column='TodayCost', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    counted = models.IntegerField(db_column='Counted', blank=True, null=True)  # Field name made lowercase.
    invpricerul = models.TextField(db_column='InvPriceRul', blank=True, null=True)  # Field name made lowercase.
    reordercsh = models.BigIntegerField(db_column='ReOrderCsh', blank=True, null=True)  # Field name made lowercase.
    reorderinv = models.BigIntegerField(db_column='ReOrderInv', blank=True, null=True)  # Field name made lowercase.
    eta = models.TextField(db_column='ETA', blank=True, null=True)  # Field name made lowercase.
    uslocalexch = models.DecimalField(db_column='USLocalExch', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    onordqty = models.IntegerField(db_column='OnOrdQty', blank=True, null=True)  # Field name made lowercase.
    ordertype = models.TextField(db_column='OrderType', blank=True, null=True)  # Field name made lowercase.
    req = models.IntegerField(db_column='Req', blank=True, null=True)  # Field name made lowercase.
    stk = models.IntegerField(db_column='Stk', blank=True, null=True)  # Field name made lowercase.
    qpv = models.IntegerField(db_column='QPV', blank=True, null=True)  # Field name made lowercase.
    sl = models.IntegerField(db_column='SL', blank=True, null=True)  # Field name made lowercase.
    sl2 = models.IntegerField(db_column='SL2', blank=True, null=True)  # Field name made lowercase.
    tl = models.IntegerField(db_column='TL', blank=True, null=True)  # Field name made lowercase.
    rl = models.IntegerField(db_column='RL', blank=True, null=True)  # Field name made lowercase.
    wl = models.IntegerField(db_column='WL', blank=True, null=True)  # Field name made lowercase.
    bd1l = models.IntegerField(db_column='BD1L', blank=True, null=True)  # Field name made lowercase.
    impl = models.IntegerField(db_column='ImpL', blank=True, null=True)  # Field name made lowercase.
    bd2l = models.IntegerField(db_column='BD2L', blank=True, null=True)  # Field name made lowercase.
    keyid = models.IntegerField(db_column='KeyId', blank=True, null=True)  # Field name made lowercase.
    ts = models.IntegerField(db_column='Ts', blank=True, null=True)  # Field name made lowercase.
    rs = models.IntegerField(db_column='Rs', blank=True, null=True)  # Field name made lowercase.
    supercededkeyid = models.IntegerField(db_column='supercededkeyId', blank=True, null=True)  # Field name made lowercase.
    crefsid = models.IntegerField(blank=True, null=True)
    costpricelast = models.IntegerField(db_column='CostPriceLast', blank=True, null=True)  # Field name made lowercase.
    suggestqty = models.IntegerField(db_column='SuggestQty', blank=True, null=True)  # Field name made lowercase.
    dynitem = models.IntegerField(db_column='DynItem', blank=True, null=True)  # Field name made lowercase.
    decstockitem = models.IntegerField(db_column='DecStockItem', blank=True, null=True)  # Field name made lowercase.
    purchcomment = models.TextField(db_column='PurchComment', blank=True, null=True)  # Field name made lowercase.
    ordergroup = models.TextField(db_column='OrderGroup', blank=True, null=True)  # Field name made lowercase.
    orderref = models.TextField(db_column='OrderRef', blank=True, null=True)  # Field name made lowercase.
    volumecost = models.DecimalField(db_column='VolumeCost', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    weightcost = models.DecimalField(db_column='WeightCost', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vcostfactor = models.DecimalField(db_column='VCostFactor', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    wcostfactor = models.DecimalField(db_column='WCostFactor', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lp = models.IntegerField(db_column='LP', blank=True, null=True)  # Field name made lowercase.
    ds = models.IntegerField(db_column='DS', blank=True, null=True)  # Field name made lowercase.
    supplier = models.TextField(db_column='Supplier', blank=True, null=True)  # Field name made lowercase.
    qty3mths = models.IntegerField(db_column='Qty3Mths', blank=True, null=True)  # Field name made lowercase.
    cref = models.TextField(db_column='CRef', blank=True, null=True)  # Field name made lowercase.
    superceded = models.TextField(db_column='Superceded', blank=True, null=True)  # Field name made lowercase.
    smc = models.CharField(db_column='SMC', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nmm = models.IntegerField(db_column='NMM', blank=True, null=True)  # Field name made lowercase.
    euro = models.DecimalField(db_column='Euro', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    del_field = models.IntegerField(db_column='Del', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    maingroup = models.TextField(db_column='MainGroup', blank=True, null=True)  # Field name made lowercase.
    bo = models.IntegerField(db_column='Bo', blank=True, null=True)  # Field name made lowercase.
    sh = models.IntegerField(db_column='Sh', blank=True, null=True)  # Field name made lowercase.
    wrk = models.IntegerField(db_column='Wrk', blank=True, null=True)  # Field name made lowercase.
    searchfield = models.TextField(db_column='SearchField', blank=True, null=True)  # Field name made lowercase.
    piclink = models.TextField(blank=True, null=True)
    need = models.IntegerField(db_column='Need', blank=True, null=True)  # Field name made lowercase.
    uniqueid = models.IntegerField(db_column='uniqueId', blank=True, null=True)  # Field name made lowercase.
    info = models.TextField(db_column='Info', blank=True, null=True)  # Field name made lowercase.
    catgroup = models.TextField(db_column='CatGroup', blank=True, null=True)  # Field name made lowercase.
    binloc11 = models.TextField(db_column='BinLoc11', blank=True, null=True)  # Field name made lowercase.
    binloc12 = models.TextField(db_column='BinLoc12', blank=True, null=True)  # Field name made lowercase.
    binloc13 = models.TextField(db_column='BinLoc13', blank=True, null=True)  # Field name made lowercase.
    binloc14 = models.TextField(db_column='BinLoc14', blank=True, null=True)  # Field name made lowercase.
    binloc15 = models.TextField(db_column='BinLoc15', blank=True, null=True)  # Field name made lowercase.
    binloc16 = models.TextField(db_column='BinLoc16', blank=True, null=True)  # Field name made lowercase.
    binloc17 = models.TextField(db_column='BinLoc17', blank=True, null=True)  # Field name made lowercase.
    binloc18 = models.TextField(db_column='BinLoc18', blank=True, null=True)  # Field name made lowercase.
    binloc19 = models.TextField(db_column='BinLoc19', blank=True, null=True)  # Field name made lowercase.
    binloc20 = models.TextField(db_column='BinLoc20', blank=True, null=True)  # Field name made lowercase.
    otherref01 = models.TextField(db_column='OtherRef01', blank=True, null=True)  # Field name made lowercase.
    otherref02 = models.TextField(db_column='OtherRef02', blank=True, null=True)  # Field name made lowercase.
    otherref03 = models.TextField(db_column='OtherRef03', blank=True, null=True)  # Field name made lowercase.
    otherref04 = models.TextField(db_column='OtherRef04', blank=True, null=True)  # Field name made lowercase.
    otherref05 = models.TextField(db_column='OtherRef05', blank=True, null=True)  # Field name made lowercase.
    otherref06 = models.TextField(db_column='OtherRef06', blank=True, null=True)  # Field name made lowercase.
    otherref07 = models.TextField(db_column='OtherRef07', blank=True, null=True)  # Field name made lowercase.
    otherref08 = models.TextField(db_column='OtherRef08', blank=True, null=True)  # Field name made lowercase.
    otherref09 = models.TextField(db_column='OtherRef09', blank=True, null=True)  # Field name made lowercase.
    otherref10 = models.TextField(db_column='OtherRef10', blank=True, null=True)  # Field name made lowercase.
    onhold = models.IntegerField(db_column='OnHold', blank=True, null=True)  # Field name made lowercase.
    onholdremark = models.TextField(db_column='OnHoldRemark', blank=True, null=True)  # Field name made lowercase.
    repflag1 = models.IntegerField(db_column='RepFlag1', blank=True, null=True)  # Field name made lowercase.
    repflag2 = models.IntegerField(db_column='RepFlag2', blank=True, null=True)  # Field name made lowercase.
    repflag3 = models.IntegerField(db_column='RepFlag3', blank=True, null=True)  # Field name made lowercase.
    repflag4 = models.IntegerField(db_column='RepFlag4', blank=True, null=True)  # Field name made lowercase.
    dircostexcl = models.DecimalField(db_column='DirCostExcl', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    avgcostexcl = models.DecimalField(db_column='AvgCostExcl', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dircostincl = models.DecimalField(db_column='DirCostIncl', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    avgcostincl = models.DecimalField(db_column='AvgCostIncl', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    priceformula = models.TextField(db_column='PriceFormula', blank=True, null=True)  # Field name made lowercase.
    repflag5 = models.IntegerField(db_column='RepFlag5', blank=True, null=True)  # Field name made lowercase.
    repflag6 = models.IntegerField(db_column='RepFlag6', blank=True, null=True)  # Field name made lowercase.
    nondiscitm = models.IntegerField(db_column='NonDiscItm', blank=True, null=True)  # Field name made lowercase.
    whlimit2 = models.DecimalField(db_column='WhLimit2', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dynmarkup = models.IntegerField(db_column='DynMarkup', blank=True, null=True)  # Field name made lowercase.
    repflag7 = models.IntegerField(db_column='RepFlag7', blank=True, null=True)  # Field name made lowercase.
    repflag8 = models.IntegerField(db_column='RepFlag8', blank=True, null=True)  # Field name made lowercase.
    repflag9 = models.IntegerField(db_column='RepFlag9', blank=True, null=True)  # Field name made lowercase.
    vloc01 = models.DecimalField(db_column='vLoc01', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vloc02 = models.DecimalField(db_column='vLoc02', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vloc03 = models.DecimalField(db_column='vLoc03', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vloc04 = models.DecimalField(db_column='vLoc04', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vloc05 = models.DecimalField(db_column='vLoc05', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vloc06 = models.DecimalField(db_column='vLoc06', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vloc07 = models.DecimalField(db_column='vLoc07', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vloc08 = models.DecimalField(db_column='vLoc08', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vloc09 = models.DecimalField(db_column='vLoc09', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vloc10 = models.DecimalField(db_column='vLoc10', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vdefq01 = models.DecimalField(db_column='vDefQ01', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vdefq02 = models.DecimalField(db_column='vDefQ02', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vdefq03 = models.DecimalField(db_column='vDefQ03', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vdefq04 = models.DecimalField(db_column='vDefQ04', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vdefq05 = models.DecimalField(db_column='vDefQ05', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vdefq06 = models.DecimalField(db_column='vDefQ06', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vdefq07 = models.DecimalField(db_column='vDefQ07', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vdefq08 = models.DecimalField(db_column='vDefQ08', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vdefq09 = models.DecimalField(db_column='vDefQ09', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vdefq10 = models.DecimalField(db_column='vDefQ10', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    serialitem = models.IntegerField(db_column='SerialItem', blank=True, null=True)  # Field name made lowercase.
    serialref = models.TextField(db_column='SerialRef', blank=True, null=True)  # Field name made lowercase.
    loc21 = models.DecimalField(db_column='Loc21', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc22 = models.DecimalField(db_column='Loc22', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc23 = models.DecimalField(db_column='Loc23', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc24 = models.DecimalField(db_column='Loc24', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc25 = models.DecimalField(db_column='Loc25', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc26 = models.DecimalField(db_column='Loc26', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc27 = models.DecimalField(db_column='Loc27', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc28 = models.DecimalField(db_column='Loc28', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc29 = models.DecimalField(db_column='Loc29', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc30 = models.DecimalField(db_column='Loc30', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc31 = models.DecimalField(db_column='Loc31', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc32 = models.DecimalField(db_column='Loc32', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc33 = models.DecimalField(db_column='Loc33', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc34 = models.DecimalField(db_column='Loc34', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc35 = models.DecimalField(db_column='Loc35', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc36 = models.DecimalField(db_column='Loc36', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc37 = models.DecimalField(db_column='Loc37', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc38 = models.DecimalField(db_column='Loc38', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc39 = models.DecimalField(db_column='Loc39', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    loc40 = models.DecimalField(db_column='Loc40', max_digits=22, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    autosearch = models.TextField(db_column='AutoSearch', blank=True, null=True)  # Field name made lowercase.
    autotrf_encode = models.TextField(blank=True, null=True)
    brandorigin = models.TextField(db_column='BrandOrigin', blank=True, null=True)  # Field name made lowercase.
    stkcatcode = models.BigIntegerField(db_column='stkCatCode', blank=True, null=True)  # Field name made lowercase.
    stkimkcode = models.BigIntegerField(db_column='stkImkCode', blank=True, null=True)  # Field name made lowercase.
    stkitmcode = models.BigIntegerField(db_column='stkItmCode', blank=True, null=True)  # Field name made lowercase.
    stkgencode = models.TextField(db_column='stkGenCode', blank=True, null=True)  # Field name made lowercase.
    barc01 = models.TextField(db_column='BarC01', blank=True, null=True)  # Field name made lowercase.
    barc02 = models.TextField(db_column='BarC02', blank=True, null=True)  # Field name made lowercase.
    barc03 = models.TextField(db_column='BarC03', blank=True, null=True)  # Field name made lowercase.
    barc04 = models.TextField(db_column='BarC04', blank=True, null=True)  # Field name made lowercase.
    barc05 = models.TextField(db_column='BarC05', blank=True, null=True)  # Field name made lowercase.
    barc06 = models.TextField(db_column='BarC06', blank=True, null=True)  # Field name made lowercase.
    barc07 = models.TextField(db_column='BarC07', blank=True, null=True)  # Field name made lowercase.
    barc08 = models.TextField(db_column='BarC08', blank=True, null=True)  # Field name made lowercase.
    barc09 = models.TextField(db_column='BarC09', blank=True, null=True)  # Field name made lowercase.
    barc10 = models.TextField(db_column='BarC10', blank=True, null=True)  # Field name made lowercase.
    syncdt = models.DateTimeField(db_column='SyncDT', blank=True, null=True)  # Field name made lowercase.
    invpricerulq = models.TextField(db_column='InvPriceRulQ', blank=True, null=True)  # Field name made lowercase.
    cshpricerul = models.TextField(db_column='CshPriceRul', blank=True, null=True)  # Field name made lowercase.
    cshpricerulq = models.TextField(db_column='CshPriceRulQ', blank=True, null=True)  # Field name made lowercase.
    images = models.TextField(db_column='Images', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'eztb3105'
